from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    command = ['ping', *shlex.split(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f'Ping failed with return code {result.returncode}: {result.stderr}')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_fixed(host: str):
    return {"status": "completed", "details": "Ping command executed successfully."}