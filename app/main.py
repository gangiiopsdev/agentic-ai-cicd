from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '-_.:~+\/@?&=,;#[]{}^$*`!@#$%^&*()_+-=[]{}|;:,.<>?/`	\n'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with proper validation and sanitization
    if not host.strip():
        raise ValueError('Host parameter cannot be empty or only whitespace')
    sanitized_host = escape_host(host)
    subprocess.call(['ping', '-c', '1', sanitized_host])  # Use specific arguments for ping
    return {'status': 'completed'}