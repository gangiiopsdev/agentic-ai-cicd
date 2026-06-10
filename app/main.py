from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Ensure host input is sanitized or use a whitelist of allowed hosts
    if not host.strip().replace('.', '').isnumeric():
        return {"status": "failed", "error": "Invalid host format"}
    result = safe_ping(['ping', host])
    return {"status": "completed", "result": result}