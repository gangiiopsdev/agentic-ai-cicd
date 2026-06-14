from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ('.', '-', '_'))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {
            "status": "completed",
            "output": result.stdout,
            "error": None
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "output": None,
            "error": e.stderr
        }