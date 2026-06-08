from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        return {'status': 'completed', 'output': 'Invalid host'}
    command = ['ping', '-c', '4', host]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return f'Command failed with error code {e.returncode}: {e.stderr}'

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[0-9a-fA-F:.]+$', host):
        return {'status': 'completed', 'output': 'Invalid host'}
    return safe_ping(host)