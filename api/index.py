from flask import Flask, render_template
import subprocess, time, keyboard
import multiprocessing, os

app = Flask(__name__)


#ctrlc = keyboard.press_and_release('ctrl+c')

def simulate_ctrl_c():
    time.sleep(2)
    keyboard.press_and_release('ctrl+c')
    run_flask_and_quit()
    return "sqd"


@app.route("/")
def page_web_de_mort():
    simulate_ctrl_c()  # Appeler la fonction pour simuler Ctrl+C
    return render_template('index.php')


def run_flask_and_quit():
    # process pour run Flask
    print(2)
    try:
        subprocess.run(['python3', '../bot.py'], timeout=5)
    except:
        pass

    
app.run()   

