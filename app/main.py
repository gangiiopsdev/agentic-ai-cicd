from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    # Implement your logic to check if the host is safe
    return True
def run_ping_command(host):
    sanitized_host = subprocess.quote(host)
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=False)
    return result.stdout, result.stderr@app.get("/ping")
def ping(host: str):    if is_safe_host(host):        stdout, stderr = run_ping_command(host)        return {"status": "completed", "stdout": stdout, "stderr": stderr}    else:        return {"error": "Invalid host"}