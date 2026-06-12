from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    for arg in args:
        if any(char in arg for char in (';', '&', '|', '`')):
            raise ValueError('Invalid character detected in command argument')
    subprocess.run(args, check=True)

    return {'status': 'completed'}