from fastapi import FastAPI
import subprocess
import shlex
import ipaddress

def safe_ping(host: str) -> str:
    try:
        ip = ipaddress.ip_address(host)
        if isinstance(ip, (ipaddress.IPv4Address, ipaddress.IPv6Address)):
            args = ['ping'] + [shlex.quote(h.strip()) for h in shlex.split(str(ip))]
            output = subprocess.run(args, capture_output=True, text=True, check=True, shell=False)
            return output.stdout
        else:
            raise ValueError('Invalid IP address')
    except ValueError as e:
        raise ValueError(e)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'output': result}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}