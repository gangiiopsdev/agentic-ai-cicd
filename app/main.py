from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Validate input
        raise HTTPException(status_code=400, detail="Invalid host")
    output = safe_ping(host)
    return {"status": "completed", "output": output}