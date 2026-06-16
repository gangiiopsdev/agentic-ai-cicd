from fastapi import FastAPI
import subprocess
import ipaddress

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate host to ensure it's a valid IP address or hostname
        ipaddress.ip_address(host)
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}