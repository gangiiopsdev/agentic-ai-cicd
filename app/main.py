from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['127.0.0.1', 'localhost']

def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    sanitized_host = sanitize_input(host)
    result = subprocess.run(["ping", sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}