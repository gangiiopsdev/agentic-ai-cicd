from fastapi import FastAPI
import subprocess
def escape_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

cmd = ['ping', '--', escape_host(host)]
popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = popen.communicate()
if error:
    raise Exception('Error occurred while pinging the host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}