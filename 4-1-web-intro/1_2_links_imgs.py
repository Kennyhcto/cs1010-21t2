from flask import Flask
from pyhtml import html, title, body, p, a, img, br, head, link

app = Flask(__name__)

@app.route('/')
def hello():
    code = html(
        head(
            title("Second PyHTML Program"),
            link(rel="stylesheet", href="static/style2.css")
        ),
        body(
            p("Hello everyone!!"),
            a(href="https://www.google.com/", target="_blank")("Go to Google!"),
            br(),
            img(src="https://images.unsplash.com/photo-1515879218367-8466d910aaa4?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2250&q=80", width="200px")
        )
    )
    #return ""
    #return "nope"
    return str(code)

if __name__ == "__main__":
    app.run(debug=True)