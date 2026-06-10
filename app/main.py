from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    return ''.join(c if c.isalnum() or c in ('.', '-', '_') else '_' for c in host)

@app.get('/ping')
def ping(host: str):
    safe_host = escape_host(host)
    if not all(c.isalnum() or c in ('.', '-', '_') for c in safe_host):
        return {'status': 'invalid input'}
    # Secure implementation
    subprocess.call(['ping', shlex.quote(safe_host)])
    return {'status': 'completed'}