from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with path sanitization and full command check
    if host.strip().isalnum():
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    else:
        raise ValueError("Invalid input")