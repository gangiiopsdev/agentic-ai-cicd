from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = shlex.split('ping ' + host)
    try:
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}