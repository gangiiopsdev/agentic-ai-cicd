from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.process = None

    def safe_ping(self, host):
        args = ['ping', *shlex.split(host)]
        self.process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return self.process.communicate()

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result, error = safe_ping_instance.safe_ping(host)
    if error:
        return {"status": "failed", "error": error.decode('utf-8')}
    return {"status": "completed", "result": result.decode('utf-8')}