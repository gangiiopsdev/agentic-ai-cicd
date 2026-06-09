from fastapi import FastAPI
import subprocess
def sanitize_input(value):
    return ''.join(e for e in value if e.isalnum() or e in ['.', '-', '_'])

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Add allowed hosts here
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host"}
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(['ping', '-c', '1', f'/bin/ping', sanitized_host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}