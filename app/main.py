from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isnumeric():
        return False
    cmd = ['ping', '-c', '4', host]
    return subprocess.run(cmd, capture_output=True, text=True)

app = FastAPI()
@app.get('/ping')
def ping_host(host: str):
    result = safe_ping(host)
    if result.returncode == 0:
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'failed'}