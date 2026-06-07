from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=10)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output.decode('utf-8')}\n' + '\n'.join(e.stderr.decode('utf-8').splitlines()[:2])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.strip():
        return {'status': 'error', 'result': 'Host parameter is required'}
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}