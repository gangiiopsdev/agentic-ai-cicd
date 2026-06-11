from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host is sanitized before passing it to the command line
    if not all(c.isalnum() or c in '.,-_' for c in host):
        raise ValueError("Invalid characters in hostname")
    subprocess.run(['ping', host], check=True)

@app.get="/ping")
def ping(host: str):