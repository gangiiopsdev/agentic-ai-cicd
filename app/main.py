from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return output.stdout
    except Exception as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid input")
    return {'status': safe_ping(host)}