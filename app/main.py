from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    validate_host(host)
    subprocess.call(['ping', host])
    return {"status": "completed"}