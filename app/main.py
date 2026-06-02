from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Input validation for the 'host' parameter
    if not host or len(host) > 255:
        raise ValueError("Invalid host parameter")
    args = ['ping'] + shlex.split(host)
    subprocess.run(args)

app = FastAPI()

@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping_safe(host: str):
    safe_ping(host)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=80)