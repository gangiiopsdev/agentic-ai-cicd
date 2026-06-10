from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError("Invalid hostname")
    args = ['ping', '--', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "stderr": str(e)}