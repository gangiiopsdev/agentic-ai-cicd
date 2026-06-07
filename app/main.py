from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}