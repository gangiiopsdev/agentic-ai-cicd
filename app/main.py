from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more valid hosts as needed
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

def resolve_hostname(hostname):
    try:
        result = subprocess.run(['nslookup', hostname], check=True, capture_output=True, text=True)
        lines = result.stdout.splitlines()
        for line in lines:
            if 'Address' in line:
                ip = line.split()[-1]
                return ip.strip()
    except subprocess.CalledProcessError:
        raise ValueError('Failed to resolve hostname')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    resolved_ip = resolve_hostname(host)
    command = ['ping', resolved_ip]
    result = subprocess.run(command, check=True, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}