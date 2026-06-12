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
    # Validate and sanitize the input before using it in the command
    if not host.isalnum():
        raise ValueError("Invalid input")
    SafeCommandRunner.safe_run("ping", shlex.split(host))
    return {"status": "completed"}