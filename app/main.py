from fastapi import FastAPI
import subprocess
globals = { '__builtins__': {} }
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.call(args, shell=False, env=globals)
    return {'status': 'completed'}