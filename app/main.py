from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Implement logic to validate the host input
    return host.replace('.', '_').isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid host input"}, 400
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}