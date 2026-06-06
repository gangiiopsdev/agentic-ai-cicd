from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            cmd = ['ping', host]
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    # Sanitize input to avoid shell injection
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    cmd = ['ping', host]
    result = subprocess.run(cmd, stderr=subprocess.STDOUT, text=True)
    return SafePing.ping(host)