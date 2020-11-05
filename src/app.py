from flask import Flask, render_template

app = Flask(__name__, template_folder='conversion')

@app.route('/')
def html(htmlFile):
    return render_template(htmlFile); 

if __name__ == '__main__':
    app.run()