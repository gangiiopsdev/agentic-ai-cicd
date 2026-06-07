from fastapi import FastAPI
import subprocess
call = subprocess.run

app = FastAPI()

@app.get('/ping')
def ping_safe(host: str):
    if not host.isdigit() and len(host) <= 15:
        result = call(['ping', host], shell=False, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Invalid input'}, 400