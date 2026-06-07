from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return arg.replace('`', '`\``).replace('$', '\$').replace('\', '\\\\')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    try:
        result = subprocess.run(['ping', f'"{escaped_host}"'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}