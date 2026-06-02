from fastapi import FastAPI
import subprocess
global_process = None

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    global global_process
    if host and isinstance(host, str) and all(c.isalnum() or c in ('.', '-', ':') for c in host):
        if global_process is not None and global_process.poll() is None:
            global_process.terminate()
        command = ['ping', host]
        try:
            global_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        except Exception as e:
            return {'error': str(e)}
    else:
        return {'error': 'Invalid input'}

    return {'status': 'completed'}