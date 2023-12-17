from flask import Flask, render_template, request, session, flash, redirect, url_for
import os
import openai
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import json
import os

app = Flask(__name__)



    

@app.route('/', methods=['GET', 'POST'])
def index():
    image_url0 = None
    image_url1 = None
    image_url2 = None
    if request.method == 'POST':
        description = request.form['desc']
        style = request.form['style']

     
        client = openai.OpenAI(api_key=os.environ.get('secret_key'))

        try:
            response1 = client.images.generate(
                model="dall-e-3",
                prompt=description + " in " + style + " style",
                size="1024x1024",
                quality="standard",
                n=1,
            )
            response2 = client.images.generate(
                model="dall-e-2",
                prompt=description + " in " + style + " style",
                size="1024x1024",
                quality="standard",
                n=1,
            )
            response3 = client.images.generate(
                model="dall-e-2",
                prompt=description + " in " + style + " style",
                size="1024x1024",
                quality="standard",
                n=1,
            )

            if response1 and response1.data:
                image_url0 = response1.data[0].url
            if response2 and response2.data:
                image_url1 = response2.data[0].url
            if response3 and response3.data:
                image_url2 = response3.data[0].url
             
        except Exception as e:
            print(f"An error occurred: {e}")

    return render_template('index.html', url0=image_url0,url1=image_url1,url2=image_url2)
