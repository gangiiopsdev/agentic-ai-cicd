from fastapi import FastAPI
import subprocess
def escape_argument(arg):
    return arg.replace(';', '').replace('&', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        safe_host = escape_argument(host)
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}