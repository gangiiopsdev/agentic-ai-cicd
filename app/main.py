from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = ['ping', 'example.com']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to avoid command injection
    sanitized_host = subprocess.list2cmdline([host])
    SafePing().ping_command[1] = sanitized_host
    try:
        result = subprocess.run(SafePing().ping_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}