from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output.decode("utf-8")}'

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    if 'localhost' in host or '127.0.0.1' in host:
        return {'status': 'completed', 'result': safe_ping(host)}
    else:
        return {'error': 'Invalid host'}