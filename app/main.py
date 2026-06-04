from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Sanitize the host input by ensuring it does not contain harmful characters
        if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', host], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed"}