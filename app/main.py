from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    # Implement your logic to check if the host is safe
    return True
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"error": "Invalid host"}
    sanitized_host = subprocess.quote(host)
    result = subprocess.run(["ping", sanitized_host], capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}