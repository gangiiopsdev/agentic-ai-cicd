from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    if host.startswith("127.") or host.startswith("localhost"):  # Example whitelist
        try:
            subprocess.run(["ping", host], check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": str(e)}
    return {"status": "completed"}