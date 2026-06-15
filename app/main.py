from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Simple sanitization, in production use a proper library or function
    return ''.join(e for e in input_str if e.isalnum() and 'a' <= e <= 'z')

def safe_ping(sanitized_host):
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    return safe_ping(sanitized_host)