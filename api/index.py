from flask import Flask, render_template
import subprocess, os

app = Flask(__name__)

@app.route("/")
def page_web_de_mort():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    subprocess.Popen(['python3', os.path.join(current_directory, 'bot.py')])
    #return "<html><body><img src='https://i.giphy.com/KmHueA88mFABT9GkkR.gif'><iframe src='https://timmy-host.vercel.app/api/bot' onload='setInterval(function(){this.src=this.src},4000)'></iframe></body></html>"
    return "test"
if __name__ == "__main__":
    app.run()
