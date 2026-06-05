from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host.isalnum() or len(host) > 255:
            raise ValueError("Invalid host input")
        command = ['ping', *shlex.split(host)]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}