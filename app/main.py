from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run with shell=False and args parameter
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid host name")
    
    output = safe_ping(host)
    return {"status": "completed", "output": output}