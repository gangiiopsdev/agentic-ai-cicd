from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output, 'utf-8')

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    return {'status': 'completed', 'output': safe_ping(host)}

def is_safe_host(host):
    # Implement logic to validate the host
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts