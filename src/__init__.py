import os
import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, render_template, request, jsonify
# import util

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/get_cred',methods=['POST'])
    def get_cred():
        errors = []
        result = ''
        try:
            url = request.form['url']
            r = requests.get(url)
            # print(r.text)
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
            return render_template('index.html', errors=errors)
        if r:
            soup = bs(r.content, 'html.parser')
            elems = soup.find_all('section')
            for elem in elems:
                result = result + " " + elem.get_text()
            
            return result
        return ''

    return app