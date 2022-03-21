from flask import Flask, render_template
app = Flask(__name__)
import ConsoleWar1st
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/my-link/')
def my_link():
    print ('I got clicked!')
    ConsoleWar1st.beginGame()
    
    savePath = os.getcwd() + '/templates'
    fileName = 'results.txt'
    completeName = os.path.join(savePath, fileName)

    with open(completeName, 'r') as f:
       return render_template('results.txt', text=f.readlines())

if __name__ == '__main__':
  app.run(debug=True)
