from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    # Validate and sanitize host input
    if not host.isdigit():
        raise ValueError("Invalid host input")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        status = run_ping(host)
        return {"status": "completed", "output": status}
    except ValueError as e:
        return {"error": str(e)}