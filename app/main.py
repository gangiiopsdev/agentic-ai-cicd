from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    def __init__(self):
        pass

    @staticmethod
def ping(host: str):
        args = ['ping', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    SafeSubprocess.ping(host)
    return {"status": "completed"}