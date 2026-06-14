from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid input'}
    # Validate IP address format
    try:
        ip_parts = host.split('.')
        if len(ip_parts) != 4 or any(not part.isdigit() or not 0 <= int(part) <= 255 for part in ip_parts):
            return {'status': 'failed', 'error': 'Invalid IP address'}
    except AttributeError:
        pass
    return safe_ping(host)