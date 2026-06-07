from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host input to ensure it does not contain harmful characters and uses a whitelist of allowed protocols
        if all(c.isalnum() or c in ['.', '-', ' ', ':', '/'] for c in host) and any(host.startswith(proto) for proto in ['http://', 'https://']):
            subprocess.call(["ping", host])
            return {"status": "completed"}
        else:
            raise ValueError("Invalid host name")
    except Exception as e:
        return {"error": str(e)}