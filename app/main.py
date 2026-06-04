from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host to prevent command injection
    if not host or ' ' in host:
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', '-c', '1'] + shlex.split(shlex.quote(host)), check=True, capture_output=True, text=True)
    return {"status": "completed", "response": result.stdout}