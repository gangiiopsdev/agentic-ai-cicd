from fastapi import FastAPI
import subprocess
def escape_host(host):
    import re
    return re.sub(r'[^a-zA-Z0-9.-]', '', host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    try:
        output = subprocess.check_output(['ping', '-c', '1', escaped_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}