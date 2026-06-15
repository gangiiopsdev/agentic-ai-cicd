from fastapi import FastAPI
import re
import subprocess
def escape_host(host):
    return re.sub(r'[^a-zA-Z0-9.-]', '', host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    try:
        result = subprocess.run(['ping', '-c 1', '--'] + [escaped_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}