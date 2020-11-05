from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def html(htmlFile):
    return './conversion/' + htmlFile

if __name__ == '__main__':
    app.run()