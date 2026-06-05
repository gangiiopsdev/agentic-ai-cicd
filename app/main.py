from fastapi import FastAPI
import subprocess
cmd = ['ping', host]
try:
    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=5)
    return {'status': 'completed', 'output': output.decode('utf-8')}
except subprocess.CalledProcessError as e:
    return {'status': 'error', 'error': e.output.decode('utf-8')}