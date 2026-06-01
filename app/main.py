from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid host parameter")
    args = ['ping', 'echo', host]  # Use echo as a safe wrapper
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}