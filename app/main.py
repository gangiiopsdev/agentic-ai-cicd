from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_call(command: str) -> None:
        args = shlex.split(command)
        try:
            subprocess.run(args, check=True)
        except subprocess.CalledProcessError as e:
            print(f'Command {command} returned non-zero exit status {e.returncode}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    SafeSubprocess.safe_call(f'ping {host}')
    return {"status": "completed"}