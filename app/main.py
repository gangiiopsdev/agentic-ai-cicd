from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('-', '.', ':', '@'))
def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of safe hosts
    return host in allowed_hosts
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Host not allowed'}
    sanitized_host = sanitize_input(host)
    try:
        command = ['ping', '-c', '1'] + shlex.split(sanitized_host)
        genesis = subprocess.run(command, capture_output=True, text=True, check=False)
        output = genesis.stdout.strip()
        if genesis.returncode != 0:
            error = genesis.stderr.strip()
            raise Exception(error)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}