from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(args):
        safe_args = [shlex.quote(arg) for arg in args]
        subprocess.run(safe_args, check=True)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    SafeSubprocess.call(args)
    return {"status": "completed"}