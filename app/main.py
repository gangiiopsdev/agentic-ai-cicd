from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not host.replace('.', '').isdigit():
            raise ValueError("Invalid host input")
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}