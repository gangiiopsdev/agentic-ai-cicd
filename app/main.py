from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['-', '.', '_', ':', '@'])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(f'ping {sanitized_host}', shell=True, check=True)
    return {"status": "completed"}