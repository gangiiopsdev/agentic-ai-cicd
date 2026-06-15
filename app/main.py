from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    # Implement proper sanitization logic here
    return user_input

class SafePing:
    def __init__(self, allowed_hosts=None):
        self.allowed_hosts = set(allowed_hosts or [])

    def is_host_allowed(self, host):
        return host in self.allowed_hosts

app = FastAPI()
ping_safe = SafePing(allowed_hosts=['127.0.0.1', '::1'])

@app.get('/ping')
def ping(host: str):
    if not ping_safe.is_host_allowed(host):
        return {'error': 'Host not allowed'}

    sanitized_host = sanitize_input(host)
    try:
        # Secure implementation with shell=False and argument list
        subprocess.run(['ping', sanitized_host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}