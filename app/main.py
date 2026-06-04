from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Sanitize input using a whitelist or regex pattern
        allowed_hosts = ['example.com', 'localhost']
        if host not in allowed_hosts:
            return 'Invalid host'
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Failed to ping {host}: {e.output.decode('utf-8')}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return {'status': safe_ping(host)}