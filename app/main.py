from fastapi import FastAPI
import subprocess
import shlex

class SanitizedSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        sanitized_command = ['ping', '-c', '1'] + shlex.split(command)
        return subprocess.run(sanitized_command, check=True, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = SanitizedSubprocess.run(host)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}