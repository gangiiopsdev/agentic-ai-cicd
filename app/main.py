from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Add your sanitization logic here
    return input_string
def safe_ping(host: str):
    if not host or 'ping' not in host.lower():
        raise ValueError('Invalid host')
    sanitized_host = subprocess.shlex_quote(host)
    try:
        output = subprocess.check_output(["ping", sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}
    return response