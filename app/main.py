from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Implement a proper input sanitization function here
    return ''.join(c for c in input_string if c.isalnum())
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', '-c', '1', sanitized_host]
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed'}