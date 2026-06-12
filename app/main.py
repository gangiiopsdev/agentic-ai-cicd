from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command, *args):
    try:
        result = subprocess.run([command] + list(args), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

@app.get("/ping")
def ping(host: str):
    # Enhanced security implementation
    if host.isalnum() and '&&' not in host and ';' not in host and '|' not in host:
        output = execute_safe_command('ping', host)
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'failed', 'error': 'Invalid input'}