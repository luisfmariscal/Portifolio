from flask import Flask, render_template, redirect, request, flash
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.secret_key = 'Fernando'


class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)