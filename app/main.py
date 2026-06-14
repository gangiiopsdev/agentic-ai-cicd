from fastapi import FastAPI
import subprocess
def get_command(host: str) -> list:
    return ['ping', host]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(get_command(host), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}