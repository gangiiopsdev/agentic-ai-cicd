from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    args = shlex.split(f'ping {shlex.quote(host)}')
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        if '1 received' in result.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed"}