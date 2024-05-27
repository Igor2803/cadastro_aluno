import os
from flask import Flask
from main import *


app = Flask(__name__)


@app.route("/")
def index():
    return alunos()
janela.mainloop()

