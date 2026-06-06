from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c if c.isalnum() or c in ['-', '.', '_'] else '_' for c in host)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    try:
        output = subprocess.check_output(['ping', '-c', '1', '--'], stderr=subprocess.STDOUT, text=True, input=safe_host.encode())
        return {'output': output}
    except subprocess.CalledProcessError as e:
        return {'error': e.output}