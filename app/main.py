from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        raise HTTPException(status_code=400, detail="Invalid host parameter")
    args = ['ping', f'-c 1 {host}']  # Limit ping count for security
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}