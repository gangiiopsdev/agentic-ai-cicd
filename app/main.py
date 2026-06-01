from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement your logic to check if the host is safe
    return True

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        # Sanitize input before using it in subprocess call
        sanitized_host = subprocess.quote(host)
        result = subprocess.run(["ping", sanitized_host], capture_output=True, text=True, check=False)
        return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}
    else:
        return {"error": "Invalid host"}