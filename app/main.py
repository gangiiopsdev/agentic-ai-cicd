from fastapi import FastAPI
import subprocess

def sanitize_input(input_str: str) -> str:
    # Sanitize or validate user input here
    return input_str.strip()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.run(['ping', f'-c 1 {sanitized_host}'], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}