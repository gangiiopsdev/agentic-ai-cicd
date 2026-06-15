from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Sanitize host input by using a whitelist or regex pattern
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return f'Error: {host} is not allowed'
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout


def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'result': response}