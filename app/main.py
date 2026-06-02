from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    try:
        subprocess.run(["ping", host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    # Secure implementation
    try:
        subprocess.run(["ping", host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}