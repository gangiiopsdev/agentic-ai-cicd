from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum():
        return {"error": "Invalid host parameter"}
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}