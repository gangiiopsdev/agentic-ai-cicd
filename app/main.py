from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    # Add your own logic to check if the host is safe to ping
    return '127.0.0.1' == host

app = FastAPI()

def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Unsafe host'}
    result = subprocess.run(['ping', f'/bin/ping {host}'], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}