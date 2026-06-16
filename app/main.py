from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if 'ping' not in host:
        return False
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

class SafePing:
    def __init__(self):
        self.allowed_hosts = {'localhost', '127.0.0.1'}

    def ping(self, host: str) -> str:
        if host in self.allowed_hosts:
            return safe_ping(host)
        else:
            return 'Unauthorized host'

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    result = safe_ping_instance.ping(host)
    return {'status': result}