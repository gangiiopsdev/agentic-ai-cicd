from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit() or e in [',', '.', ':', '-', '_', '@'])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"status": "invalid host"}
    # Using subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}