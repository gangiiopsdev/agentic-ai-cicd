from fastapi import FastAPI
import re
import subprocess
from ipaddress import ip_address, IPv4Address, IPv6Address

app = FastAPI()

def ping(host: str):
    try:
        # Validate IP address
        if ':' in host:
            ip_address(host)
        else:
            int(ip_address(host))
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except (ValueError, AttributeError) as e:
        return {'status': 'error', 'message': str(e)}

# Additional recommendation: Use a more secure method for hostname validation if possible.
# Example: Validate against a list of allowed hosts or use DNS resolution to ensure the host exists.