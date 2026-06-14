from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    if not all(arg.isalnum() for arg in args[1:]) and not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host provided')
    subprocess.run(args, check=True)
    return {'status': 'completed'}