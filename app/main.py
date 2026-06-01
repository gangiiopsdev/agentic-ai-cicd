from fastapi import FastAPI
import subprocess
import shlex

global host_list
host_list = ['example.com']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    if host not in host_list:
        return {"error": "Invalid host"}
    command = ['ping', *shlex.split(host)]
    subprocess.run(command, check=True)

    return {"status": "completed"}