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
        # Validate input to prevent injection attacks
        if not host.isalnum() or '-' in host:
            raise ValueError("Invalid host name")
        command = ['ping', shlex.quote(host)]
        output = subprocess.run(command, capture_output=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}