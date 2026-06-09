from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Basic input sanitization (not comprehensive)
    return ''.join(e for e in input_string if e.isalnum() or e in ['.', '-', '_'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": subprocess.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}