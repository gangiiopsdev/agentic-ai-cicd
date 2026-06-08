from fastapi import FastAPI
import subprocess
class ShellEscapeError(Exception):
    pass

def shell_escape(input_str):
    for char in "$&*()|\<>[]{};'", '"':
        if char in input_str:
            raise ShellEscapeError(f'Input contains forbidden character: {char}')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        shell_escape(host)
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}