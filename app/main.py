from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with a list of arguments to avoid shell injection
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate the input to ensure it only contains allowed characters
    if not all(c.isalnum() or c in [ '.', '-', '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')'] for c in host):
        raise ValueError("Invalid input")
    return ping(host)