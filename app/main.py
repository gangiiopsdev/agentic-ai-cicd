from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(value: str) -> str:
    # Implement your sanitization logic here
    return value.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}