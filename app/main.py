from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.Popen with shell=False and safe args
    import shlex
    command = ["ping", *shlex.split(host)]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        raise Exception(f'Ping failed with error: {error.decode()}')

    return {'status': 'completed'}