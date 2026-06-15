from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def call(command: str):
        args = command.split()
        for arg in args:
            if not arg.isalnum():
                raise ValueError('Invalid argument')
        subprocess.call(args, shell=False)

app = FastAPI()

@app.get("/", include_in_schema=False)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafeSubprocess.call(f'ping {host}')
    return {"status": "completed"}