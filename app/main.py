from fastapi import FastAPI
import subprocess
import shlex
class SanitizedSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        sanitized_command = ' '.join(shlex.quote(arg) for arg in command.split())
        return subprocess.run(sanitized_command, capture_output=True, text=True, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host:
        return {"status": "failed", "error": "No host provided"}
    try:
        result = SanitizedSubprocess.run('ping', host)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}