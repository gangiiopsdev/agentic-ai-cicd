from fastapi import FastAPI
import subprocess
host_whitelist = ['127.0.0.1', '::ffff:127.0.0.1']
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in host_whitelist:
        return {'error': 'Host not allowed'}
    subprocess.call(['ping', '--', host])
    return {'status': 'completed'}