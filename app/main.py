from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use a full path for the ping executable to avoid potential issues
        output = subprocess.run(['/usr/bin/ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    safe_host = ''.join(e for e in host if e.isalnum() or e in ('.', '-', '_'))
    result = safe_ping(safe_host)
    return {"status": "completed", "output": result}

# Add additional validation and logging for security