from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if host.isnumeric():
        try:
            output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}
    else:
        return {'status': 'Invalid input'}