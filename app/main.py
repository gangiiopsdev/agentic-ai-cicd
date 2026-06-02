from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    sanitized_host = host.strip().replace(' ', '_')
    try:
        subprocess.check_output(["ping", sanitized_host], stderr=subprocess.STDOUT, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}

    return {"status": "completed"}