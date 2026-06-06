from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid input for host")
    subprocess.run(["ping", f'"{host}"'], capture_output=True, text=True)
    return {"status": "completed"}