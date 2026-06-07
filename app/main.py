from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('-', '.', ':', '@'))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = subprocess.list2cmdline(shlex.split(sanitize_input(host)))
    try:
        genesis = subprocess.run(['ping', '-c', '1'] + [sanitized_host], capture_output=True, text=True, check=False)
        output = genesis.stdout.strip()
        if genesis.returncode != 0:
            error = genesis.stderr.strip()
            raise Exception(error)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}