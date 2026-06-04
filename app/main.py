from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Add your sanitization logic here
    return ''.join(c for c in input_str if c.isalnum() or c in '._-')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}