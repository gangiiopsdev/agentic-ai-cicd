from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

def validate_ip_address(ip_address):
    parts = ip_address.split('.')
    if len(parts) != 4:
        raise ValueError('Invalid IP address')
    for part in parts:
        try:
            int(part)
        except ValueError:
            raise ValueError('Invalid IP address')
        if not (0 <= int(part) <= 255):
            raise ValueError('Invalid IP address')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        validate_ip_address(host)
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}
    sanitized_host = sanitize_host(host)
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True, text=True, capture_output=True)
    return {'status': 'completed'}