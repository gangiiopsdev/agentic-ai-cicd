from fastapi import FastAPI
import subprocess
def escape_shell(command):
    return command.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_shell(host)
    try:
        subprocess.run(['ping', escaped_host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': f'Ping failed with error: {e}'}
    return {'status': 'completed'}