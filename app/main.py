from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def safe_call(command: str, *args, **kwargs):
        args = shlex.split(command)
        return subprocess.run(args, *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = SafeSubprocess.safe_call(f'ping', host)
        return {"status": "completed", "output": result.stdout.decode()}
    except Exception as e:
        return {"status": "failed", "error": str(e)}