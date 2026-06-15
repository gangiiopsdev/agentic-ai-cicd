from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['127.0.0.1', '::1']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in globally_safe_hosts:
        raise HTTPException(status_code=403, detail='Unauthorized host')
    try:
        result = subprocess.run(['ping', '--'] + [host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}