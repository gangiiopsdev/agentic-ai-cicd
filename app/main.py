from fastapi import FastAPI
import subprocess

def run_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it does not contain malicious characters
    if not host.isalnum() and not '.' in host:
        return {"error": "Invalid host parameter"}
    output = run_ping(host)
    return {"status": "completed", "output": output}