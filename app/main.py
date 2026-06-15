from fastapi import FastAPI
import subprocess
import shlex

class SanitizedSubprocess:
    @staticmethod
def quote(command: str) -> str:
        return ' '.join(shlex.quote(arg) for arg in command.split())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the host input to avoid shell injection
        sanitized_host = subprocess.quote(host)
        command = f'ping {sanitized_host}'
        result = subprocess.run(SanitizedSubprocess.quote(command), capture_output=True, text=True, shell=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}