import subprocess

def run_bot():
    try:
        subprocess.run(['python3', 'bot.py'])
    except:
        pass
    return "TEST"
       
