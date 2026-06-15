from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input before using it in the command
    if not host.isalnum():
        raise ValueError('Invalid host input')
    cmd = ['ping', quote(host)]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}