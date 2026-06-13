from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Implement proper sanitization logic here
    return input_string.strip()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation
    subprocess.run(["ping", sanitized_host], check=True, capture_output=True)
    return {"status": "completed"}