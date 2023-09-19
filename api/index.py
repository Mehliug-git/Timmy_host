from flask import Flask, render_template
import subprocess, time
import multiprocessing, os

app = Flask(__name__)



@app.route("/")
def page_web_de_mort():

    #obligé seulement sur vercel snn ça marche po 
    run_flask_and_quit()
    le_bot()
    run_flask()
    return render_template('index.php'),200


def run_flask_and_quit():
    # process pour run Flask
    process = multiprocessing.Process(target=app.run)

    # Start le process app.run Flask
    process.start()

    time.sleep(5)

    #Kill le process Flask
    process.terminate()
    

def run_flask():
    # process pour run Flask
    process = multiprocessing.Process(target=app.run)

    # Start le process app.run Flask
    process.start()

    time.sleep(5)

    #Kill le process Flask
    process.terminate()


def le_bot():
    os.system("python3 bot.py")



if __name__ == "__main__":
    
    app.run()
