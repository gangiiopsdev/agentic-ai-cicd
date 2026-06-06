from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts  # Return a boolean value indicating if the host is valid
def get_ip_address(hostname):
    try:
        output = subprocess.check_output(['nslookup', hostname], text=True)
        for line in output.splitlines():
            if 'Address:' in line and len(line) > len('Address:'):  # Check if the line contains an IP address
                return line.strip().split()[-1]
    except subprocess.CalledProcessError:
        pass
    return None
def safe_ping(hostname):
    ip_address = get_ip_address(hostname)
    if validate_host(ip_address) and ip_address:
        result = subprocess.run(['ping', '-c', '1', ip_address], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Invalid host or unable to resolve hostname"}
app = FastAPI()
@app.get("/ping")
def ping(hostname: str):
    return safe_ping(hostname)