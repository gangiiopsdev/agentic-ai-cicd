from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate the host parameter
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError('Invalid hostname')

    # Use a secure way to call subprocess without shell=True
    args = ['ping', '-c', '4', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):    safe_ping(host)    return {"status": "completed"}