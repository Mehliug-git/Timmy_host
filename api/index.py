from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def page_web_de_mort():
    bot_process = subprocess.Popen(['python3', '/api/bot.py'])
    return "<html><body><img src='https://i.giphy.com/KmHueA88mFABT9GkkR.gif'></body></html>"

if __name__ == "__main__":
    app.run()
