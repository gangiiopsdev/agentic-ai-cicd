from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Simple sanitization example, more robust methods should be used in production
    return ''.join(e for e in input_str if e.isalnum() or e in ['-', '.', '_'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Using subprocess.run instead of subprocess.call and avoiding shell=True
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}