from fastapi import FastAPI
import subprocess
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with check=True and capture_output=True for better error handling and output capturing.
    try:
        result = subprocess.run(shlex.split(f"ping {shlex.quote(host)}"), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}