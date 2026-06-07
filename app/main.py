from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        subprocess.run(["ping", host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}