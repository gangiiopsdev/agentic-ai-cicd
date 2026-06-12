from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host.strip().isdigit() or '.' not in host:
        raise ValueError("Invalid host format")
app = FastAPI()
@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get="/ping"
def ping(host: str):
    validate_host(host)
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}