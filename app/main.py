from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(c if c.isalnum() or c in '.-' else '' for c in input_string)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safer implementation using subprocess.run to avoid shell=True
    result = subprocess.run(['ping', '-c 1', sanitized_host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}