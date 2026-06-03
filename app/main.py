from fastapi import FastAPI
import subprocess
def escape_shell_argument(arg):
    return ''.join(c if c.isalnum() else '_' for c in arg)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    escaped_host = escape_shell_argument(host)
    result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}