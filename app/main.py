from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_user_input(input):
    return subprocess.list2cmdline(input.split())

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    subprocess.call(escape_user_input(['ping', host]))
    return {'status': 'completed'}