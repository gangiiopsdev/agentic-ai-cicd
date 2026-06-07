from fastapi import FastAPI
import subprocess
import shlex
def safe_run(command):
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout
class SafePing:
    def __init__(self):
        pass

    async def ping(self, host: str):
        # Define a whitelist of allowed hosts
        allowed_hosts = ['example.com', 'test.local']
        if host not in allowed_hosts:
            raise ValueError('Invalid host')

        sanitized_host = ''.join(e for e in host if e.isalnum() or e.isdigit() or e in ('.', '-', '_'))
        command = ['ping', sanitized_host]
        output = safe_run(command)
        return {'status': 'completed', 'output': output}
class SafeApp:
    def __init__(self):
        self.safe_ping = SafePing()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return await safe_app.safe_ping.ping(host)
safe_app = SafeApp()