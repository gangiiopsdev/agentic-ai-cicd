from fastapi import FastAPI
import subprocess

async def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    return True  # Return a boolean value indicating if the host is valid

def get_ip_address(hostname):
    try:
        output = subprocess.check_output(['nslookup', hostname], text=True)
        for line in output.splitlines():
            if 'Address:' in line and len(line) > len('Address:'):  # Check if the line contains an IP address
                return line.strip().split()[-1]
    except subprocess.CalledProcessError:
        pass
    return None

app = FastAPI()

@app.get("/ping")
def ping(hostname: str):
    ip_address = get_ip_address(hostname)
    if validate_host(ip_address) and ip_address:
        result = subprocess.run(['ping', '-c', '1', ip_address], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Invalid host or unable to resolve hostname"}