from fastapi import FastAPI
import subprocess
def sanitize_input(input):
    if '&&' in input or ';' in input or '|' in input:
        raise ValueError('Invalid characters detected in input')
    return input
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(f"ping {sanitized_host}", shell=False, check=True, text=True)
    return {"status": "completed"}