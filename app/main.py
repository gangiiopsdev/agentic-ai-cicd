from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']  # Define a list of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")

    # Secure implementation using check_output and safe input handling
    subprocess.run(['ping', host], capture_output=True, text=True)

    return {"status": "completed"}