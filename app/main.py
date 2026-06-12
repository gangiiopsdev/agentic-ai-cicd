from fastapi import FastAPI
import subprocess
import ipaddress
globally_banned_hosts = ['192.168.1.1', '10.0.0.1']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in globally_banned_hosts:
        return {'status': 'banned'}
    try:
        # Validate the IP address format using ipaddress module
        ipaddress.ip_address(host)
        subprocess.run(['ping', '-c 1', host], check=True, timeout=5)
        return {'status': 'completed'}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': str(e)}