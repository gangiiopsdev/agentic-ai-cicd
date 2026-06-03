from fastapi import FastAPI
import subprocess
get_shell_access = False  # Control variable to prevent shell access by default

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not get_shell_access:
        subprocess.call(f'ping {host}', shell=False)
    else:
        raise Exception("Shell access is disabled")

    return {"status": "completed"}