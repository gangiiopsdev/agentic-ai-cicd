from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and list of arguments
    safe_host = ''.join(c for c in host if c.isalnum() or c in '._-')  # More robust sanitization example
    subprocess.run(['ping', '-c', '1', safe_host], check=True)
    return {"status": "completed"}