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
        # Validate the host input to ensure it does not contain harmful characters
        if all(c.isalnum() or c in ['.', '-'] for c in host): 
            subprocess.call(["ping", host])
            return {"status": "completed"}
        else:
            raise ValueError("Invalid host name")
    except Exception as e:
        return {"error": str(e)}