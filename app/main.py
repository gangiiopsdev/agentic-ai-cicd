from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    if not all(c.isalnum() or c in [',', '.', ' '] for c in user_input):
        raise ValueError('Invalid input')

@app.get("/ping")
def ping(host: str):
    try:
        sanitize_input(host)
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}