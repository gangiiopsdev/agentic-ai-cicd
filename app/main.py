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
    # Validate and sanitize the host input before using it in the command
    sanitized_host = shlex.quote(host)
    result = subprocess.run(["ping", sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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