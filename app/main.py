from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    if not host.isalnum():  # Add input validation
        return False
    args = shlex.split(f'ping {shlex.quote(host)}')
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        if '1 received' in result.stdout:
            return True
        else:
            print(f'Ping failed: {result.stderr}')
            return False
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}
{e.stderr}')
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