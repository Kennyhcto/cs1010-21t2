from flask import Flask
from pyhtml import html, form, label, head, body, input_, title, p

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    pass



if __name__ == "__main__":
    app.run(debug=True)