from flask import Flask, render_template
import subprocess

app = Flask(__name__)
bot_process = subprocess.Popen(['python3' , '../bot.py'])


@app.route("/")
def page_web_de_mort():
    bot_process
    return "<html><body><img src='https://i.giphy.com/KmHueA88mFABT9GkkR.gif'></body></html>"
    
