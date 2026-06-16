from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    return all(c.isalnum() or c in ('.', '-') for c in host)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}

    # Use a safe way to execute the command without shell injection risks
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    return {"status": "completed"}