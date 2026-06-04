from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', '--', host]  # Adding '--' to prevent command injection
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'stdout': output.decode(), 'stderr': error.decode()}
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}