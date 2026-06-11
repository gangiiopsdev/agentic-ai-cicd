from fastapi import FastAPI
import subprocess
def generate_ping_command(host):
    return ['ping', host]
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(generate_ping_command(host), capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error {e.stderr}'}, 400