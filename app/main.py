from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isnumeric():
        return False, None
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
        return True, output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return False, e.output.decode('utf-8')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    success, result = safe_ping(host)
    if not success:
        return {'status': 'failed', 'error': result}
    return {'status': 'completed', 'result': result}