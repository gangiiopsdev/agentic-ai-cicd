from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.run without shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the input to ensure it's safe
        if not host.isalnum() or '..' in host:
            raise ValueError('Invalid host')
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except Exception as e:
        return {"error": str(e), "status": "failed"}