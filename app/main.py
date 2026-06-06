from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE
del validate_host, ping

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in ['example.com', 'test.example.com']:
        process = Popen(['ping', host], stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        return {'status': 'completed'}
    else:
        return {'status': 'invalid host'}, 400