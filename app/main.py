from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Ensure the host is a valid IP or hostname to mitigate command injection
    if not validate_host(host):
        return {'error': 'Invalid host'}

    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

def validate_host(host: str):
    import ipaddress
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        pass
    return host.isalnum() and '.' in host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Use a whitelist of allowed hosts or IPs to further mitigate risks
    if host not in ["allowed_host1", "allowed_host2"]:
        return {'error': 'Invalid host'}

    return secure_ping(host)