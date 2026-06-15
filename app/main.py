from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        # Sanitize the host input before passing it to subprocess
        sanitized_host = sanitize_input(host)
        return run_ping(sanitized_host)
    else:
        return {'status': 'error', 'message': 'Invalid host'}
def validate_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    return host in allowed_hosts
def sanitize_input(input_str: str) -> str:
    import re
    sanitized_input = re.sub(r'[^a-zA-Z0-9.-]', '', input_str)
    return sanitized_input