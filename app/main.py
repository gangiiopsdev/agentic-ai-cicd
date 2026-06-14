from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isdigit() or int(host) < 1 or int(host) > 254:
        return {'error': 'Invalid host'}

    # Use subprocess.Popen with list of arguments to avoid shell=True
    process = subprocess.Popen(['ping', '-c', '4', str(host)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        return {'error': error.decode()}
    return {'status': 'completed'}