from flask import Flask, Blueprint

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hi there'

