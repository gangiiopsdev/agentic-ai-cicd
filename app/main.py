from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isspace())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', shlex.quote(sanitized_host)], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}