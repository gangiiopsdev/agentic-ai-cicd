from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def safe_ping(host: str):
        ping_command = ['ping'] + shlex.split(host)
        return subprocess.call(ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    result = SafePing.safe_ping(host)
    return {'status': 'completed', 'result': result}