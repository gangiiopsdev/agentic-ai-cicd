from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input
    if not all(c.isalnum() or c in '-_.@' for c in host):
        return {"status": "failed", "error": "Invalid characters in host name"}
    try:
        result = subprocess.run(["ping", '-c', '1', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}