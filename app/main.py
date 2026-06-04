from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_'))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    escaped_host = escape_host(host)
    try:
        output = subprocess.run(['ping', escaped_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}