from fastapi import FastAPI
import subprocess
global pinger
pinger = subprocess.Popen(['ping', '-c', '1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global pinger
    if host == 'localhost':
        output, error = pinger.communicate()
        return {"status": "completed", "output": output.decode(), "error": error.decode()}
    else:
        return {"status": "denied"}