from flask import Flask
import urllib.request, time
import multiprocessing

app = Flask(__name__)

@app.route("/")
def page_web_de_mort():
    
    run_flask()
    #return "<html><body><img src='https://i.giphy.com/KmHueA88mFABT9GkkR.gif'><iframe src='https://timmy-host.vercel.app/api/bot' onload='setInterval(function(){this.src=this.src},4000)'></iframe></body></html>"
    return "test"

def run_flask():
    # process pour run Flask
    process = multiprocessing.Process(target=app.run)

    # Start le process app.run Flask
    process.start()
    time.sleep(2)
    #Kill le process Flask
    process.terminate()
    try:

        urllib.request.urlopen("https://timmy-host.vercel.app/api/bot", timeout=2)
    except:
        pass

if __name__ == "__main__":
    
    while True:
        run_flask()

