from fastapi import FastAPI
import subprocess
global host_list = ['127.0.0.1', '8.8.8.8']
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if host not in global host_list:
        return {'error': 'Invalid host'}
    subprocess.call(['ping', '-c', '4', host])
    return {'status': 'completed'}