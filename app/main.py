from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isnumeric():
        raise ValueError('Invalid host')
    command = ['ping', '-c', '1', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout, result.stderr
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        output, error = safe_ping(host)
        if error:
            return {'error': error}
        else:
            return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'error': str(e)}