from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Secure implementation
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    safe_ping = SafePing()
    # Validate host to ensure it is a valid IP address or hostname
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')
    return safe_ping.ping(host)