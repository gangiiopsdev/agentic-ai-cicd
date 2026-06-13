from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return shlex.quote(input_str)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and properly formatted arguments
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', sanitized_host], check=True, text=True, capture_output=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}