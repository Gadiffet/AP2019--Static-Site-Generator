from flask import Flask, render_template

app = Flask(__name__, template_folder='conversion')

def html(htmlFile):
    fileHTML = htmlFile
    return fileHTML

@app.route('/')
def index(fileHTML):
    return render_template(fileHTML); 

if __name__ == '__main__':
    app.run()