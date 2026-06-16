from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate and sanitize host input before using it in subprocess
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    subprocess.run(['ping', *shlex.split(host)], check=True, text=True)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        ping_result = subprocess.run(['ping', *shlex.split(host)], check=True, text=True)
        return {"status": "completed", "result": ping_result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}