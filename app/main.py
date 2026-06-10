from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['.', '-', '_', '@'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.quote(sanitize_input(host))  # Use quote to escape shell metacharacters
    args = ['ping', sanitized_host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}