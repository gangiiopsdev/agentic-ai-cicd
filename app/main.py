from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use a whitelist of allowed hosts or domains
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        try:
            args = ['ping', host]
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
    else:
        return 'Invalid host'

def ping(host: str):
    return {'status': safe_ping(host)}