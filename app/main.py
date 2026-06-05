from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):    
    return {'status': 'completed'}

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., allow only certain hosts or IP addresses.
    return True