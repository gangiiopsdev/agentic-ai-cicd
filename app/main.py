from fastapi import FastAPI
import subprocess
def safe_subprocess(command, *args):
    try:
        result = subprocess.run([command] + list(args), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    output = safe_subprocess('ping', '-c', '1', host.replace(';', '').replace('&', ''))
    return {'status': 'completed', 'output': output}