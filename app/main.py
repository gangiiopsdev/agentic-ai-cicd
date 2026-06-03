from fastapi import FastAPI
import subprocess
import re
class SafeSubprocess:
    @staticmethod
def safe_ping(host: str):
        cmd = ['ping', host]
        try:
            output = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed", "output": output.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "output": e.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    return SafeSubprocess.safe_ping(host)