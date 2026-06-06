from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = shlex.split(f'ping {host}')
    # Use check_output instead of call to capture output and handle errors more gracefully
    try:
        result = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Error: {e.output.decode('utf-8')}'

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}