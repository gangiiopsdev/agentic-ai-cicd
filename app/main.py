from fastapi import FastAPI
import subprocess
from html import escape
def sanitize_input(value: str) -> str:
    # Implement your sanitization logic here
    return escape(value)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}