from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    # Validate and sanitize the input
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid hostname"}
    command = ['ping', host]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        return {"error": str(error.decode('utf-8'))}
    return {"status": "completed", "output": output.decode('utf-8')}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)