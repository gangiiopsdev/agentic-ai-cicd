from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent command injection
    if not is_valid_host(host):
        return {"error": "Invalid host input"}
    # Safer implementation using subprocess.run with shell=False and properly formatted arguments
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}