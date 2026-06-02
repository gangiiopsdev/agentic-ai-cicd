from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote
def escape_shell_arg(arg):
    return ' '.join([shell_quote(a) for a in arg.split()])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', escape_shell_arg(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}