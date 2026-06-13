from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_call(command, *args, **kwargs):
        args = [shlex.quote(arg) for arg in args]
        command += ' '.join(args)
        return subprocess.call(command, shell=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    subprocess.call(SafeSubprocess.safe_call(f'ping', host), shell=True)

    return {"status": "completed"}