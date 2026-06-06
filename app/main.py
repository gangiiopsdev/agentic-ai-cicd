from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_input(input):
    return ''.join(c if c.isalnum() or c in '._-' else '_' for c in input)

@app.get('/ping')
def ping(host: str):
    try:
        escaped_host = escape_shell_input(host)
        args = ['ping', *shlex.split(escaped_host)]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}