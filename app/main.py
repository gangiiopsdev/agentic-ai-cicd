from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self, max_size=1024):
        self.max_size = max_size

    def ping(self, host: str) -> str:
        # Validate the host to ensure it does not contain malicious characters
        if not host.replace('.', '').isdigit():
            raise ValueError('Invalid host')
        # Use shlex.quote to safely escape the host input
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            return str(result.stderr)
        output = result.stdout.split('\n')
        for i in range(len(output)):
            if len(output[i]) > self.max_size:
                output[i] = output[i][:self.max_size]
                output[i] += '...'
        return '\n'.join(output)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_ping = SafePing()
    try:
        return safe_ping.ping(host)
    except ValueError as e:
        return str(e)