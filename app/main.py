from fastapi import FastAPI
import subprocess
app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    try:
        result = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = result.communicate()
        return output.decode(), error.decode()
    except Exception as e:
        return None, str(e)

@app.get("/ping")
def ping(host: str):
    output, error = safe_ping(host)
    if output is not None:
        return {'status': 'completed', 'output': output, 'error': error}
    else:
        return {'status': 'failed', 'error': error}