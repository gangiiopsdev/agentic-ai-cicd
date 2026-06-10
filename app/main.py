from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Validate host input
    if not host.isalnum():
        raise ValueError('Invalid host name')

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    args = ['ping', '-c', '1', safe_ping(host)]\n    subprocess.run(args, check=True, text=True, capture_output=True)
    return {"status": "completed", "output": result.stdout}