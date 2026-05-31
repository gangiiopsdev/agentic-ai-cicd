from fastapi import FastAPI
import subprocess
import shlex
def safe_getinput(command):
    args = shlex.split(command)
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout.strip()

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = safe_getinput(f'ping -c 4 {host}')
        return {"status": "completed", "result": result}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}