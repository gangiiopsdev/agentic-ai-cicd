from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        try:
            output = subprocess.check_output(['ping', f'"{host}"'], stderr=subprocess.STDOUT, universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.output)}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)