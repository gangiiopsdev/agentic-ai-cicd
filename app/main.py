from fastapi import FastAPI
import subprocess
import shlex

global pinger
pinger = subprocess.Popen(['ping', '-c', '4'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = pinger.communicate(input=host.encode())
        return {"status": "completed", "output": result.decode()}
    except Exception as e:
        return {"error": str(e)}