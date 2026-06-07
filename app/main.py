from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_call(command: str, *args: str):
        args = [arg.encode().decode('unicode_escape') for arg in args]
        subprocess.run([command] + list(args), check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafeSubprocess.safe_call('ping', host)
    return {"status": "completed"}