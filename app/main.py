from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f'Error pinging {host}: {e}'

class SafePing:
    def __init__(self):
        self.allowed_hosts = set(['127.0.0.1', '::1'])  # Add other allowed hosts here

    def ping(self, host: str):
        if host in self.allowed_hosts:
            return safe_ping(host)
        else:
            return 'Unauthorized host'

global_safe_ping = SafePing()

@app.get("/ping")
def ping(host: str): return {'status': global_safe_ping.ping(host)}