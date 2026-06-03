from fastapi import FastAPI
import subprocess
import shlex

class SafeHostValidator:
    def __init__(self):
        self.allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')

    def validate(self, host: str) -> bool:
        return all(c in self.allowed_chars for c in host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    validator = SafeHostValidator()
    if not validator.validate(host):
        return {'status': 'error', 'output': 'Invalid hostname'}
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', f'-c 1 {safe_host}'], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return {'status': 'error', 'output': str(result.stderr)}
    return {'status': 'completed', 'output': result.stdout}