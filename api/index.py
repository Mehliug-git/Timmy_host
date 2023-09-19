from flask import Flask, render_template
import subprocess, time
import multiprocessing, os

app = Flask(__name__)



@app.route("/")
def page_web_de_mort():

    return render_template('index.php')

def run_flask_and_quit():
    
    try:
        subprocess.run(['python3', 'bot.py'], timeout=5)
    except:
        pass

    app.run()
    

run_flask_and_quit()