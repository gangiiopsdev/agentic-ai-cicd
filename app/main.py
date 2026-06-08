from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_input(input_str):
    return all(c.isalnum() or c in '-.' for c in input_str)

@app.post('/ping/')
def ping(host: str):
    if not is_safe_input(host):
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}