from fastapi import FastAPI
import subprocess
def sanitize_input(value):
    return ''.join(e for e in value if e.isalnum() or e in ['.', '-', '_'])
def validate_ip(ip_address):
    parts = ip_address.split('.')
    if len(parts) != 4:
        raise ValueError('Invalid IP address')
    for part in parts:
        if not part.isdigit() or int(part) < 0 or int(part) > 255:
            raise ValueError('Invalid IP address')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        validate_ip(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(['ping', '-c', '1', f'"{sanitized_host}"'], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}