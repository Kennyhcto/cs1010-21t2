from flask import Flask, request
from pyhtml import html, title, body, label, p, table, tr, td, strong, head, form, input_
import string

app = Flask(__name__)

@app.route('/')
def main():
    code = html(
        head(
            title("Text Server")
        ),
        body(
            form(action="analyse")
            (
                input_(type="text", name="text"),
                input_(type="Submit", value="Analyse Text")
            )
        )
    )
    return str(code)

@app.route('/analyse', methods=["POST"])
def analyse_text():

    #print(f"{request.form=}")
    #print(f"all punctuation characters: {string.punctuation}")
    text = request.form['text']
    num_characters = len(text)
    num_punc = 0
    for character in text:
        if character in string.punctuation or \
            character in string.whitespace:
            num_punc += 1
    num_letters = num_characters - num_punc
    words = text.split()


    code = html(
        head(
            title("First PyHTML Program")
        ),
        body(
            p(f"Your text: {text}"),
            p(f"Number of characters: {num_characters}"),
            p(f"Number of letters: {num_letters}"),
            p(f"Number of words: {len(words)}")
        )
    )
    return str(code)

if __name__ == "__main__":
    app.run(debug=True)