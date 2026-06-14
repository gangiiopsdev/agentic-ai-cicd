from fastapi import FastAPI
import re

def safe_ping(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'error': 'Host not allowed'}
    # Use a whitelisted list of allowed hosts and validate the input more strictly
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host format'}
    # Sanitize the input before using it in subprocess.call()
    sanitized_host = f'ping {subprocess.quote(host)}'
    return subprocess.run(sanitized_host, check=True, text=True, shell=False)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return result
    else:
        return {'status': 'completed', 'output': result.stdout}