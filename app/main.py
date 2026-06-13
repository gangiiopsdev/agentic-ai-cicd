from fastapi import FastAPI
import subprocess
def escape_shell(command):
    return command.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_shell(host)
    try:
        result = subprocess.run(['ping', '-c', '1', escaped_host], check=True, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': f'Ping failed with error: {e.stderr.decode()}'}