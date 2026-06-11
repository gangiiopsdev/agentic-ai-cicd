from fastapi import FastAPI
import shlex
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    try:
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}