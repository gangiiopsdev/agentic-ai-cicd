from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isnumeric():
        return False
    cmd = ['ping', '-c', '4', host]
    return True
cmd = safe_ping(host)
if cmd:
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}
else:
    return {'status': 'failed'}