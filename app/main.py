from fastapi import FastAPI
import subprocess
from html import escape
def sanitize_input(value: str) -> str:
    # Implement your sanitization logic here
    return escape(value)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = host.strip()
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True, shell=False)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}