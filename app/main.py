from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add validation logic here, e.g., allow only certain IP ranges or hostnames.
    pass

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "Invalid host", "error": "Host not allowed."}

    # Secure implementation
    subprocess.call(['ping', host])

    return {"status": "completed"}