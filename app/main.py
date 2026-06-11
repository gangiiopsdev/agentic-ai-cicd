from fastapi import FastAPI
import subprocess
globally_banned_hosts = ['192.168.1.1', '10.0.0.1']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in globally_banned_hosts:
        return {'status': 'banned'}
    try:
        # Validate the IP address format using regex
        import re
        if not re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', host):
            return {'status': 'Invalid IP address'}
        subprocess.run(['ping', '-c 1', host], check=True, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': str(e)}