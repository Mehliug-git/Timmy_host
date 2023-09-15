from flask import Flask, render_template
import urllib.request, time

app = Flask(__name__)

@app.route("/")
def page_web_de_mort():
    
    
    #return "<html><body><img src='https://i.giphy.com/KmHueA88mFABT9GkkR.gif'><iframe src='https://timmy-host.vercel.app/api/bot' onload='setInterval(function(){this.src=this.src},4000)'></iframe></body></html>"
    return "test"






if __name__ == "__main__":
    
    while True == True:
        app.run()
        
        
        urllib.request.urlopen("https://timmy-host.vercel.app/api/bot")
        time.sleep(2)
        urllib.request.urlopen("https://timmy-host.vercel.app/api/bot")

