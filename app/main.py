from fastapi import FastAPI
import subprocess
global _ping_cache = {}

app = FastAPI()

def safe_ping(host: str):
    if host in _ping_cache:
        return _ping_cache[host]

    # Safe implementation
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True)
        result = 'success' if '64 bytes from' in output else 'failure'
        _ping_cache[host] = result
        return result
    except subprocess.CalledProcessError:
        return 'failure'

def ping(host: str):
    result = safe_ping(host)
    return {'status': result}