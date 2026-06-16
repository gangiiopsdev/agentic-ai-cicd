from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Validate the host input to ensure it only contains digits and hyphens
    if not all(c.isdigit() or c == '-' for c in host):  
        return False
    args = ['ping', '-c', '4'] + shlex.split(host)
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

def safe_host(host):
    # Use a whitelist to ensure only valid hosts are processed
    allowed_hosts = ['example.com', 'another-example.com']  
    if host not in allowed_hosts:
        return False
    return True

@app.get("/ping")
def ping(host: str):  
    if not safe_host(host):
        return {'error': 'Invalid host'}  
    output, error = safe_ping(host)
    if not output:
        return {'error': error}
    return {'status': 'completed', 'output': output}