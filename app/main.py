from fastapi import FastAPI
import subprocess
global_host = 'example.com' # Replace with a default or restricted host value

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use a whitelist to allow only certain hosts
        if host not in [global_host]:
            raise ValueError('Invalid host')
        subprocess.call(["ping", host])
    except Exception as e:
        return {"error": str(e)}
    return {"status": "completed"}