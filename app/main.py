from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add your validation logic here (e.g., allow only certain domains)
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}