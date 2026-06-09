from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host: str):
    # Use subprocess.run instead of subprocess.call with shell=True
    try:
        args = ['ping'] + shlex.split(host)
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)