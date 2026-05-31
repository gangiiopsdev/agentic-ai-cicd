from fastapi import FastAPI
import subprocess
 guarded_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if host not in guarded_hosts:
        raise Exception('Invalid host')
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}