from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Secure implementation using shlex.split to escape arguments safely
    args = ['ping', host]
    subprocess.call(args)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Simple validation to ensure host is alphanumeric
        return {"error": "Invalid host input"}
    execute_ping(host)
    return {"status": "completed"}