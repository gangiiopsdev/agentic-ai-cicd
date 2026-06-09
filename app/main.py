from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError("Invalid hostname")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}