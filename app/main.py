from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command):
        return subprocess.run(command, capture_output=True, text=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid host'}
    safe_command = ['ping', '-c', '1', host]
    result = SafeSubprocess.run(safe_command)
    return {'status': 'completed', 'output': result.stdout}