from fastapi import FastAPI
import subprocess
def validate_input(input_str):
    if 'ping' in input_str or 'shell' in input_str:
        raise ValueError('Input contains disallowed keywords')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_input(host)
    sanitized_host = host.replace(' ', '_').replace('.', '_')  # Simple validation to avoid injection
    subprocess.run(['ping', f'-c 1 {sanitized_host}'], check=True, capture_output=True, text=True)  # Limit the number of pings
    return {"status": "completed"}