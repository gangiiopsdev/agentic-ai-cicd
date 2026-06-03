from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if "ping" in host:
        return {"error": "Invalid input detected"}
    subprocess.run(['ping', host], check=True, shell=False)
    return {"status": "completed"}