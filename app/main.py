from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping/{host}')
def ping_route(host: str):
    if '@' in host or ':' in host or '>' in host or '<' in host or ';' in host or '&' in host or '$' in host or '`' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)