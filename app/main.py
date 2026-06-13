from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    if host and all(c.isalnum() or c in ('.', '-', '_') for c in host):
        safe_host = subprocess.list2cmdline([host])  # Use list2cmdline to escape shell special characters
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True)
        if result.returncode == 0:
            return {"status": "completed", "response": result.stdout}
        else:
            return {"status": "failed", "error": result.stderr}
    else:
        raise ValueError('Invalid host name')