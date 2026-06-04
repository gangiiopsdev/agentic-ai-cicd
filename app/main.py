from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def execute(host: str):
        try:
            args = shlex.split(f'ping {host}')
            subprocess.run(args, check=True)
        except subprocess.CalledProcessError as e:
            print(f'Ping failed with error: {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafePing.execute(host)
    return {"status": "completed"}