from fastapi import FastAPI
import subprocess
git_command = f'ping {host}'
if host.isnumeric():
    subprocess.call(git_command, shell=False)
else:
    raise ValueError('Invalid input')
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    git_command = f'ping {host}'
    if host.isnumeric():
        subprocess.call(git_command, shell=False)
    else:
        raise ValueError('Invalid input')
    return {"status": "completed"}