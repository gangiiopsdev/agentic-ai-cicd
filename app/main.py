from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, timeout=5)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.strip()}
    except subprocess.TimeoutExpired as e:
        return {"status": "failed", "error": "Command timed out"}