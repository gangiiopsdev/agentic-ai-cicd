from fastapi import FastAPI
import subprocess
def get_command(host: str) -> list:
    return ['ping', '-c', '1', host]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.run(get_command(host), check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}