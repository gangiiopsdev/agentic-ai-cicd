from fastapi import FastAPI
import subprocess
import shlex
class SafeCommandRunner:
    @staticmethod
def safe_run(command: str, args: List[str]):
        complete_command = [command] + list(shlex.split(args))
        subprocess.run(complete_command, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafeCommandRunner.safe_run("ping", host)
    return {"status": "completed"}