from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Use a safe method instead of shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid host input")
    output = run_ping(host)
    return {"status": "completed", "output": output}