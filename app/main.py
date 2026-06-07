from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Implement logic to validate the host input
    return all(c.isalnum() or c in ('.', '-', '_') for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid_host"}
    # Secure implementation
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}