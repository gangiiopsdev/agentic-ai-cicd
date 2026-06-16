from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return subprocess.list2cmdline([input_string])

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', '-c', '1', sanitized_host], shell=False)
    return {'status': 'completed'}