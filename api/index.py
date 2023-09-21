import os
import threading, subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def page_web_de_mort():
    # thread exec run_bot() en bg
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    return render_template('index.php')
subprocess.run(["python", "bot.py"])
def run_bot():
    # process pour exécuter le bot
    print("bot start heheheha")
    path = os.getcwd()
    subprocess.run(["python", "bot.py"])
    print(path)


if __name__ == "__main__":
    app.run()
