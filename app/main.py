from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use a whitelist of allowed hosts or implement proper validation
    if host not in ['example.com', 'test.com']:
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}

# Add input validation and sanitization for the host parameter to prevent command injection.