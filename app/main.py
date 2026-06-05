from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return ' '.join(map(shlex.quote, arg.split()))

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    try:
        result = subprocess.run(['ping', escaped_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}