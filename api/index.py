from flask import Flask, render_template
import urllib.request, time
import multiprocessing, os

app = Flask(__name__)



@app.route("/")
def page_web_de_mort():
    #obligé seulement sur vercel snn ça marche po 
    run_flask()

    return render_template('index.php'),200



def run_flask():
    # process pour run Flask
    process = multiprocessing.Process(target=app.run)

    # Start le process app.run Flask
    process.start()

    time.sleep(2)

    #Kill le process Flask
    #process.terminate()
    try:
        get = urllib.request.urlopen("https://timmy-host.vercel.app/api/bot", timeout=9)

        process2 = multiprocessing.Process(target=get)
        process2.start()
        time.sleep(10)

        process2 = multiprocessing.Process(target=get)
        process2.start()        
        time.sleep(10)
        
        process2 = multiprocessing.Process(target=get)
        process2.start()    
    except:
        pass




if __name__ == "__main__":
    
    while True:
        run_flask()

