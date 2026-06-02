from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_call(command: str, *args, **kwargs):
        return subprocess.run(command.split(), check=True, input=None, capture_output=True, text=True, *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    result = SafeSubprocess.safe_call(command)
    return {"status": "completed", "result": result.stdout}