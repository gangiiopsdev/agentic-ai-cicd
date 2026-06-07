from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        host = shlex.quote(host)  # Sanitize the input using shlex.quote
        args = ['ping', '-c', '1'] + [host]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)