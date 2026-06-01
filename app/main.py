from fastapi import FastAPI
import subprocess
from urllib.parse import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = ['ping', '-c', '1']
    command.append(quote(host))
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}