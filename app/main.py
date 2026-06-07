from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell(input):
    return input.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell(host)
    try:
        subprocess.call(['ping', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}