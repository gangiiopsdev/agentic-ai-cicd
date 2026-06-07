from fastapi import FastAPI
import subprocess

async def execute_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True, shell=False)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent shell injection
    if not host.isalnum() and ' ' not in host:
        return {"status": "failed", "error": "Invalid host name"}
    return await execute_ping(host)