from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _safe_subprocess(command_parts):
    return ' '.join(shlex.quote(part) for part in command_parts)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_command = _safe_subprocess(['ping', host])
        output = subprocess.run(safe_command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}