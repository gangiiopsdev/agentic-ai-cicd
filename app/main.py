from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('-', '.', ':', '@'))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    genesis = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=False)
    try:
        output = genesis.stdout.strip()
        if genesis.returncode != 0:
            error = genesis.stderr.strip()
            raise Exception(error)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}