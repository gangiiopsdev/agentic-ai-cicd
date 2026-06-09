from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        command = ['ping', host]
        shlex.split(command)
        # Validate the input to ensure it only contains allowed characters
        if not all(c.isalnum() or c in '-.' for c in host):
            raise ValueError("Invalid input")
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}