from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        return subprocess.run(command.split(), check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    result = SafeSubprocess.run(command)
    return {"status": "completed", "output": result.stdout}