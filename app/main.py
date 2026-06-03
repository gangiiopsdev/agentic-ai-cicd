from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host name"}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "stderr": e.stderr}

def is_valid_host(host: str) -> bool:
    # Add your validation logic here, e.g., regex to match allowed host names
    return True