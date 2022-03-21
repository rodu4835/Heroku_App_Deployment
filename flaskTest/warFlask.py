from flask import Flask, render_template, url_for, request
import ConsoleWar1st

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    return ConsoleWar1st

if __name__ == '__main__':
    app.run(debug=True)

