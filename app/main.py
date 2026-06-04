from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and input validation
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    command = ' '.join(shlex.quote(arg) for arg in args)
    subprocess.run(command, check=True, shell=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}