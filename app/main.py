from fastapi import FastAPI
import subprocess
def escape_shell(command):
    return command.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_shell(host)
    subprocess.call(['ping', escaped_host])
    return {'status': 'completed'}