from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation using subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}