from fastapi import FastAPI
import subprocess
git_path = '/usr/bin/ping'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.call([git_path, host])
    return {'status': 'completed'}