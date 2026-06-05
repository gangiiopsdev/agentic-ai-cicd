from fastapi import FastAPI
import subprocess
import re
def escape_shell_argument(arg):
    return ''.join(c for c in arg if re.match(r'[a-zA-Z0-9]', c))

global_app = FastAPI()

@globa_app.get('/ping')
def ping(host: str):
    # Secure implementation
    escaped_host = escape_shell_argument(host)
    result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}