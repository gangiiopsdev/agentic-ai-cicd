from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(c if c.isalnum() or c in ['.', '_', '-'] else '_' for c in host)

def sanitize_host(host):
    # Add additional sanitization logic as needed
    return host.strip()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(sanitize_host(host))
    subprocess.call(['ping', '-c', '1', escaped_host])  # Limit the number of pings to prevent denial of service
    return {'status': 'completed'}