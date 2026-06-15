from fastapi import FastAPI
import subprocess
git add .

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}