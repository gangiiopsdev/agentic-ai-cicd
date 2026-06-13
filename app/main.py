from fastapi import FastAPI
import subprocess
cmd = ['ping', host]
for arg in cmd:
    if isinstance(arg, str) and '&&' in arg or ';' in arg or '|' in arg or '`' in arg:
        raise ValueError('Invalid characters in command argument')
try:
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}
except subprocess.CalledProcessError as e:
    return {'status': 'failed', 'error': e.stderr}