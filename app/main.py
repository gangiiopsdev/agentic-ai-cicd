from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

def is_safe_url(url):
    parsed_url = urlparse(url)
    return all([parsed_url.scheme, parsed_url.netloc]) and parsed_url.scheme in ('http', 'https')

@app.get("/ping")
def ping(host: str):
    if not is_safe_url(f'http://{host}'):
        return {'"status": "failed", "error": "Invalid host URL"'}
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT)
        return {'"status": "completed", "output": output.decode()} 
    except subprocess.CalledProcessError as e:
        return {'"status": "failed", "error": e.output.decode()}