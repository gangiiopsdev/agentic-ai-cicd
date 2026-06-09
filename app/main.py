from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(command_parts):
    for part in command_parts:
        if isinstance(part, str) and not all(c.isalnum() or c in '-.' for c in part):
            raise ValueError('Unsafe input detected')
    return command_parts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_command = safe_ping(['ping', host])
        output = subprocess.run(safe_command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}