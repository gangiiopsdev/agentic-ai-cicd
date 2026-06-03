from fastapi import FastAPI
import subprocess
import ipaddress

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host is not allowed'}

    try:
        result = subprocess.run(['ping', str(ipaddress.ip_address(host))], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except (subprocess.CalledProcessError, ipaddress.AddressValueError) as e:
        return {'status': 'failed', 'error': str(e)}