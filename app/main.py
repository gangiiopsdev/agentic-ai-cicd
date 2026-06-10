from fastapi import FastAPI
import subprocess
from html import escape
def sanitize_input(value: str) -> str:
    # Implement your sanitization logic here
    return escape(value)

def validate_host(host: str) -> bool:
    # Add validation logic to ensure the host is a valid hostname or IP address
    return True if re.match(r'^[a-zA-Z0-9.-]+$', host) else False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        sanitized_host = sanitize_input(host)
        args = ['ping', f'-c 1 {sanitized_host}']  # Limit the number of packets to prevent DoS
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid host'}