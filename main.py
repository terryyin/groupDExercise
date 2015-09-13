from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello Group D dudes!'


@app.errorhandler(404)
def page_not_found(e):
    """whatever you are looking for we don't have. Sorry"""
    return 'no, it is not here', 404
