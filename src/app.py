from flask import Flask, render_template

app = Flask(__name__, template_folder='conversion')

@app.route('/')
def html():
    return render_template('test.html');

if __name__ == '__main__':
    app.run()