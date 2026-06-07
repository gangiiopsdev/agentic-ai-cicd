from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input):
    # Implement input sanitization here
    return ''.join(filter(str.isalnum, input))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', sanitized_host], timeout=5, check=True, capture_output=True, text=True)
        return {"status": "completed", "result": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}