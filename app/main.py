from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Sanitize the host input to prevent injection
        host = subprocess.quote(host)
        generate_ping_command = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': generate_ping_command.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}
global app
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    return ping(host)