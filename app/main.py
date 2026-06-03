from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        command = ['ping', sanitized_host]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}