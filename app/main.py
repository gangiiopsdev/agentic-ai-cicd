from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Safe implementation
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Simple validation to prevent command injection
        return {'status': 'error', 'message': 'Invalid host'}
    result = execute_ping(host)
    return {'status': 'completed', 'result': result}