from fastapi import FastAPI
import subprocess

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['-', '.', '_', '/', ':'])

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed", "output": sanitized_host.stdout.decode('utf-8')}