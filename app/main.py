from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate host input to ensure it does not contain malicious commands
        if '&&' in host or ';' in host or '|' in host or '`' in host:
            return {'status': 'error', 'message': 'Invalid input'}
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}