from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if host.strip() and all(c.isalnum() for c in host):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout,
    else:
        return None

@app.get("/ping")
def get_ping_status():
    return {"status": "completed"}