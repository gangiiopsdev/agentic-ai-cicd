from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

def sanitize_input(input_str: str) -> str:
    # Implement a proper input sanitization function here
    pass

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    return safe_ping(sanitized_host)