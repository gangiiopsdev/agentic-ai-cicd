from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize host input
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed", "result": "success"}
    except Exception as e:
        return {"status": "failed", "result": str(e)}