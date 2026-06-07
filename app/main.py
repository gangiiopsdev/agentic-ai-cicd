from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(host):
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host input')
    return host

cmd = ['ping', shlex.quote(sanitize_input(host))]
subprocess.run(cmd, check=True)
return {'status': 'completed'}