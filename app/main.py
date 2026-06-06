from fastapi import FastAPI
import subprocess
def check_host(host):
    if not host:
        raise ValueError('Host parameter is required')
    return host
def ping(host: str):
    host = check_host(host)
    command = ['ping', '-c', '1', host]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}

# Preventive controls:
# 1. Validate the input to ensure it only contains allowed characters.
# 2. Use a whitelist of allowed hosts or IP addresses.
# 3. Log all subprocess calls for auditing purposes.