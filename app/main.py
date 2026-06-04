from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(arg):
    return ''.join(c if c.isalnum() else f'\\{c}' for c in arg)

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and passing arguments as a list
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr.decode()}