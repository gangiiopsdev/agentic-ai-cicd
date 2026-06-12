from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not host.isalnum() and '.' not in host:
        raise ValueError("Invalid host name")
    try:
        result = subprocess.run(['ping', f'"{host}"'], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    return ping(host)