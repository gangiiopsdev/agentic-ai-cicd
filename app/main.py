from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        if not host.strip() or len(host.split()) > 1:
            raise ValueError("Invalid host parameter")
        sanitized_host = subprocess.list2cmdline([host])
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}