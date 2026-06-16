from fastapi import FastAPI, HTTPException
import subprocess
global blacklist = ['; ', '|', '&']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    for command in blacklist:
        if command in host:
            raise HTTPException(status_code=400, detail='Invalid input detected')

    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}