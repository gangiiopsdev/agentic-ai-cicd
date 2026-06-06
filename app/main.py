from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    # Safe implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}

# Example validation function
def validate_host(hostname: str) -> bool:
    # Simple example: only allow certain domains
    allowed_domains = ['example.com', 'test.com']
    return any(hostname.endswith(domain) for domain in allowed_domains)