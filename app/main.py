from fastapi import FastAPI
import subprocess
given_host = '127.0.0.1'  # Fixed host as a placeholder, replace with actual logic
# Whitelist of allowed hosts
allowed_hosts = ['127.0.0.1', '::1']
if given_host not in allowed_hosts:
    return {'status': 'failed', 'error': 'Host not allowed'}

try:
    output = subprocess.check_output(['ping', f'-c 4 {given_host}'], stderr=subprocess.STDOUT, text=True)
    return {'status': 'completed', 'output': output}
except subprocess.CalledProcessError as e:
    return {'status': 'failed', 'error': e.output}