from fastapi import FastAPI
import subprocess
global pinger

def ping(host: str):
    global pinger
    try:
        pinger = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = pinger.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping_host(host: str):
    return ping(host)