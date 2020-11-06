from flask import Flask, render_template

app = Flask(__name__, template_folder='conversion')

@app.route('/template')
def html(htmlFile):
    return render_template('conversion/template.html'); 

if __name__ == '__main__':
    app.run()