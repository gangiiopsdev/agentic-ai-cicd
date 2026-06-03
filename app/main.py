from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_call(command, *args, **kwargs):
        args = [shlex.quote(arg) for arg in args]
        full_command = command % tuple(args)
        subprocess.run(full_command, shell=True, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafeSubprocess.safe_call("ping %s", host)
    return {"status": "completed"}