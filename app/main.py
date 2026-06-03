from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    valid_hosts = ['127.0.0.1', 'localhost']  # Define a list of allowed hosts
    if host in valid_hosts:
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
    else:
        return 'Invalid host'
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}