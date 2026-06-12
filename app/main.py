from fastapi import FastAPI
import subprocess
def check_host(host):
    if not host.isalnum():
        raise ValueError('Invalid host name')
host = 'example.com'  # Assume this is safely provided elsewhere
ping_command = ['ping', host]
subprocess.run(ping_command, check=True)
return {'status': 'completed'}