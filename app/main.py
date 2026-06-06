from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    else:
        return {"status": "completed"}