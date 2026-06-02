from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.call(['ping', '-c', '1', re.escape(host)])  # Use -c and escape the input to prevent injection
    except Exception as e:
        return {'error': str(e)}