from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    @staticmethod
def safe_ping(host: str):
        if host.strip().isnumeric():
            return subprocess.call(['ping', *shlex.split(host)], shell=False)
        else:
            return 'Invalid input'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    return PingCommand.safe_ping(host)