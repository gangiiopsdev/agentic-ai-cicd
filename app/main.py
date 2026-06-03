from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command: list[str], **kwargs) -> subprocess.CompletedProcess:
        return subprocess.run(command, check=True, capture_output=True, text=True, **kwargs)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        ip_address = [int(i) for i in host.split('.')]
        if len(ip_address) != 4 or any(not (0 <= num <= 255) for num in ip_address):
            return {'status': 'error', 'message': 'Invalid IP address format'}
    except ValueError:
        return {'status': 'error', 'message': 'Invalid host format'}

    # Validate the host format to ensure it's a valid IP address
    if not all(host[i].isdigit() for i in range(0, len(host), 4)) or host.count('.') != 3:
        return {'status': 'error', 'message': 'Invalid host format'}

    command = ['ping', '-c', '1', shlex.quote(host)]
    result = SafeSubprocess.run(command)
    return {'status': 'completed', 'output': result.stdout}