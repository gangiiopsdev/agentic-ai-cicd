from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    if not host.isdigit():
        return False
    args = ['ping', '-c', '4'] + [arg for arg in shlex.split(host) if arg.isalnum()]  # Validate and sanitize input
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr
def validate_host(host):
    return all(c.isdigit() or c in ['-', '.', ','] for c in host)@app.get("/ping")def ping(host: str):    if not validate_host(host):
        return {'error': 'Invalid host'}    output, error = safe_ping(host)
    if not output:
        return {'error': error}
    return {'status': 'completed', 'output': output}