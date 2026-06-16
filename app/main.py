from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    # Simple hostname safety check
    return all(char.isalnum() or char in ['-', '.'] for char in hostname)

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        raise ValueError("Invalid hostname")
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}