from fastapi import FastAPI
import subprocess

global_process = None

def create_ping_process(host):
    global global_process
    if global_process and global_process.poll() is not None:
        global_process.terminate()
        global_process.wait()
    try:
        # Sanitize input to avoid command injection
        if host.strip().isdigit():
            subprocess.run(['ping', host], check=True)
        else:
            return {'error': 'Invalid input'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return create_ping_process(host)