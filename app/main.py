from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        return {"status": "invalid input"}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}