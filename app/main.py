from fastapi import FastAPI
import subprocess
def escape_input(user_input):
    return subprocess.list2cmdline([user_input])
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    escaped_host = escape_input(host)
    subprocess.call(['ping', escaped_host])
    return {'status': 'completed'}