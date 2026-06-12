from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        if 'ping' not in host and '/' not in host and '\' not in host:
            output = subprocess.run(['ping', host], capture_output=True, text=True)
            return {"status": "completed", "output": output.stdout}
        else:
            return {"status": "failed", "error": "Invalid input detected"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}