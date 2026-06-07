from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        args = ['ping', '--'] + [host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}, 403

# Add input validation and sanitization for the host parameter