import os
import threading, subprocess, time
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def page_web_de_mort():
    # thread exec run_bot() en bg
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    time.sleep(8)
    return render_template('index.php')


def run_bot():
    # process pour exécuter le bot
    print("bot start heheheha")
    test = os.system("python3 bot.py")
    bot_thread = threading.Thread(target=test)
    bot_thread.start()


run_bot()
if __name__ == "__main__":
    app.run()
