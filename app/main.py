from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping_host(host):
    try:
        # Validate host to ensure it's safe to use in the command
        if not host.strip() or 'ping' in host.lower():
            raise ValueError('Invalid host input')
        output = subprocess.check_output(shlex.split(f'ping {shlex.quote(host)}'), stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8')
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    try:
        # Validate host to ensure it's safe to use in the command
        if not host.strip() or 'ping' in host.lower():
            raise ValueError('Invalid host input')
        output = subprocess.check_output(shlex.split(f'ping {shlex.quote(host)}'), stderr=subprocess.STDOUT, timeout=5)
        return {'status': output.decode('utf-8')}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'error': str(e)}