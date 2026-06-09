from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return input_str.replace(';', '').replace('&', '')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safer implementation
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}