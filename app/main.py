from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if host in ['127.0.0.1', '::1']:  # Allow only localhost for simplicity
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True)
            return {"status": "completed", "response": result.stdout}
        except Exception as e:
            return {"status": "error", "response": str(e)}
    else:
        return {"status": "error", "response": "Invalid host"}