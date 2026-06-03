from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the host parameter
        sanitized_host = ''.join(filter(str.isalnum, host))
        output = subprocess.run(['ping', '-c 4', sanitized_host], capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e.stderr)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}