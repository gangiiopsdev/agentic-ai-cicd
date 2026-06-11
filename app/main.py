from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isnumeric():
        return False
    cmd = ['ping', '-c', '4', host]
    return True
host = '127.0.0.1'  # Example host, should be parameterized
if safe_ping(host):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}
else:
    return {'status': 'failed'}