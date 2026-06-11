from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.isnumeric():
        return subprocess.call(['ping', '-c', '4'], preexec_fn=subprocess.Popen, close_fds=True)
    else:
        raise ValueError('Invalid input for ping')

@app.get("/ping")
def ping(host: str):
    try:
        return {'status': safe_ping(host), 'message': 'Ping completed'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}