from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(c if c.isalnum() or c in '.-' else '' for c in input_string)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safer implementation
    subprocess.call(f'ping {sanitized_host}', shell=False)
    return {'status': 'completed'}