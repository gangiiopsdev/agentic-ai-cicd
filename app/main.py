from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Use shlex.quote to safely escape the input
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(f'ping {safe_host}', shell=False)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Ensure the host is safe before passing to run_ping
    if is_safe_host(host):
        run_ping(host)
        return {'status': 'completed'}
    else:
        raise ValueError('Unsafe input detected')
def is_safe_host(host: str) -> bool:
    # Implement logic to check if the host is safe
    # For example, allow only specific domains or IP addresses
    allowed_hosts = ['example.com', '192.168.1.1']
    return host in allowed_hosts