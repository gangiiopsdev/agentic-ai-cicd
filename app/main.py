from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_input(input_string):
    return input_string.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_input(host)
    try:
        subprocess.run(['ping', '-c', '1', escaped_host], check=True, text=True, capture_output=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}