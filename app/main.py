from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    return ''.join(filter(lambda char: char.isalnum() or char == '.' or char == '-', host))

global_vars = globals()
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if '@' not in sanitized_host:
        try:
            output = subprocess.check_output(['ping', '-c', '1', sanitized_host], stderr=subprocess.STDOUT, shell=False, text=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}
    else:
        return {'status': 'error', 'message': 'Invalid host'}