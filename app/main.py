from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement your safe host validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Add input validation and sanitization for the host parameter