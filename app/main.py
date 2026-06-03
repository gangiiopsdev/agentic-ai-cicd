from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Validate the input to ensure it does not contain malicious content
    if not host.isalnum() or '&&' in host or ';' in host:
        raise ValueError("Invalid input")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": result.stdout}