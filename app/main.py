from fastapi import FastAPI
import subprocess
import shlex
class SafeCommand:
    def __init__(self, *args):
        self.args = args
    def __getitem__(self, key):
        return self.args[key]
    def __iter__(self):
        return iter(self.args)
    def __len__(self):
        return len(self.args)
    def __str__(self):
        return shlex.join(self.args)

app = FastAPI()
def ping(host: str):
    # More comprehensive validation for host to prevent command injection
    if not all(c.isalnum() or c in ['-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] for c in host):
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        result = subprocess.run(SafeCommand('ping', '-c', '1', shlex.quote(host)), check=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)