from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    args = ' '.join(shlex.quote(arg) for arg in command)
    subprocess.call(args, shell=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    args = ' '.join(shlex.quote(arg) for arg in command)
    subprocess.call(args, shell=True)
    return {"status": "completed"}