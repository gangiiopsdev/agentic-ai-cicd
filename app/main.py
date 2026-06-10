from fastapi import FastAPI
import subprocess
cmd = ['ping', host]
if not all(c.isalnum() or c in '._-' for c in host):
    return {'status': 'failed', 'error': 'Invalid hostname'}
try:
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}
except Exception as e:
    return {'status': 'failed', 'error': str(e)}