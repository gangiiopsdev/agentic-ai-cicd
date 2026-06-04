from fastapi import FastAPI
import subprocess
import shlex

class SecurePing:
    def __init__(self):
        self.app = FastAPI()

    async def ping(self, host: str):
        if '@' in host or '>' in host or '<' in host or '&' in host or ';' in host or '|' in host or '`' in host:
            return {'status': 'failed', 'error': 'Invalid characters in host'}
        try:
            result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

secure_ping = SecurePing()

@app.get("/ping")
def ping_wrapper(host: str):
    return secure_ping.ping(host)