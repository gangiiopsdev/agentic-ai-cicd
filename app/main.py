from fastapi import FastAPI
import subprocess
def escape_input(input_string):
    return input_string.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_input(host)
    subprocess.run(['ping', escaped_host], check=True)
    return {'status': 'completed'}