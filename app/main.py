from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Secure implementation using subprocess.run with args tuple and proper sanitization of host input
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host provided"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

def is_valid_host(host):
    # Simple validation, can be enhanced as needed
    return host and not (' ' in host or '@' in host)