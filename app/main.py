from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell(command):
    return [arg.replace(';', '').replace('|', '').replace('&', '').replace('^', '').replace('*', '') for arg in command]

@app.get('/ping')
def ping(host: str):
    if 'ping' not in host and all(char not in host for char in ['&&', '|', ';', '`']):
        safe_host = subprocess.quote(host)
        subprocess.run(['ping', safe_host], check=True, shell=False)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid input'}