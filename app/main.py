from fastapi import FastAPI
import subprocess
import shlex
global_config = {
    'allowed_hosts': ['127.0.0.1', '::1']
}
app = FastAPI()
def run_ping(host):
    if not host or ' ' in host:
        raise ValueError("Invalid host")
    command = shlex.split(f'ping {shlex.quote(host)}')  # Use shlex.quote to sanitize input
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode()
def is_host_allowed(host):
    return any(host.startswith(allowed_host) for allowed_host in global_config['allowed_hosts'])
@app.get("/ping")
def ping(host: str):
    if not is_host_allowed(host):
        raise ValueError("Host not allowed")
    try:
        output = run_ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}