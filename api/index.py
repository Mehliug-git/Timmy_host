from flask import Flask, render_template
import subprocess, time
import multiprocessing, os

app = Flask(__name__)



@app.route("/")
def page_web_de_mort():

    #obligé seulement sur vercel snn ça marche po 
    
    #run_flask()
    
    #le_bot() 
    return render_template('index.php'), run_flask_and_quit


def le_bot():
    os.system("python3 bot.py")


def run_flask_and_quit():
    # process pour run Flask
    print(2)
    
    try:
        subprocess.run(['python3', 'bot.py'], timeout=10)
    except:
        pass

    app.run()
    

def run_flask():
    # process pour run Flask
    process = multiprocessing.Process(target=app.run(port=8089))

    # Start le process app.run Flask
    #process.start()

    time.sleep(5)
    print("sleep finit")
    #Kill le process Flask
    process.terminate()
    print("process kill")




run_flask_and_quit()