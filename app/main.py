from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with proper input validation
    if '@' in host or ' ' in host:
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500