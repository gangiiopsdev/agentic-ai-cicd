from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement input sanitization logic here
    return ''.join(e for e in input_string if e.isalnum() or e in ('.', '-'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(f'ping {sanitized_host}', shell=False, check=True)
    return {"status": "completed"}