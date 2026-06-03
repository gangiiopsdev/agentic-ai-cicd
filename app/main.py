from fastapi import FastAPI
import subprocess
class SafeCommand:
    @staticmethod
def sanitize_input(value: str) -> str:
        return ''.join(c for c in value if c.isalnum() or c == '.' or c == '-')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    host = SafeCommand.sanitize_input(host)
    # Validate the host input to prevent command injection
    if not host.strip().isalnum() or '.' not in host:
        return {'status': 'error', 'message': 'Invalid host format'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}