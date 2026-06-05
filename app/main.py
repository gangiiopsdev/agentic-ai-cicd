from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not all(c.isalnum() or c in '.-\/' for c in host):
        raise ValueError("Invalid hostname")
    process = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}