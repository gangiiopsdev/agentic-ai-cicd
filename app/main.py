from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    # Secure implementation
    command = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(shlex.quote(host))  # Prevent command injection by quoting the host parameter
    return {"status": "completed", "result": result}