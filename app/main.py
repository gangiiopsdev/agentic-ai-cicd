from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping/{host}')
def ping_host(host: str):
    try:
        git = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = git.communicate()
        return {'status': 'completed', 'stdout': output.decode('utf-8'), 'stderr': error.decode('utf-8')}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}