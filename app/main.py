from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        args = shlex.split(command)
        return subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, *args, **kwargs)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Safe implementation using SafeSubprocess.run
    subprocess.call(SafeSubprocess.run(f"ping ", host, shell=False))
    return {"status": "completed"}