from fastapi import FastAPI
import subprocess
cimport netaddr

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if netaddr.valid_ip(host):
        # Use subprocess.run instead of subprocess.call for better security
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError('Invalid IP address')