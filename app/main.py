from fastapi import FastAPI
import subprocess
cmd = ['ping', host]
if not all(x.isalnum() or x in '-.' for x in host):
    raise ValueError('Invalid hostname')
try:
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}
except subprocess.CalledProcessError as e:
    return {'status': 'failed', 'error': str(e)}