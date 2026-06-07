from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.Popen with shell=False
    args = ['ping', host]
    result = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}

@app.get("/ping")
def ping_wrapper(host: str):
    return ping(host)