from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Implement proper input sanitization here
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}