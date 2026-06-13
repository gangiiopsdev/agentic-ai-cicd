from fastapi import FastAPI
import shlex
import re
import subprocess
def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        return 'Invalid input'
    command = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, str):
        return {"error": result}
    else:
        return {"status": "completed", "output": result}