from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or len(host) > 255:
        raise ValueError('Invalid host input')
    # Validate the host to prevent command injection
    if '&&' in host or '|' in host or ';' in host or '`' in host or '&' in host:
        raise ValueError('Invalid characters detected in host input')
    return {'status': safe_ping(host)}