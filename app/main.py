from fastapi import FastAPI
import subprocess
cimport os

global app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not os.path.exists('/sbin/ping') and not os.path.exists('/bin/ping'):
        raise ValueError('Ping executable not found on the system. Check your environment settings.')
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        ping(host)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 400