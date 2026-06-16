from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_call(command, *args, **kwargs):
        args = list(args)
        for i, arg in enumerate(args):
            if isinstance(arg, str):
                args[i] = shlex.quote(arg)
        command = ' '.join([shlex.quote(c) for c in command])
        subprocess.call(command.split(), *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafeSubprocess.safe_call(["ping", host])
    return {"status": "completed"}