from fastapi import FastAPI
import subprocess
def sanitize_input(value: str) -> str:
    # Basic sanitization (e.g., removing non-alphanumeric characters)
    return ''.join(filter(str.isalnum, value))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}