from fastapi import FastAPI
import subprocess
global_pinger = ['ping', 'google.com']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in global_pinger:
        try:
            result = subprocess.run(global_pinger, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        return {'error': 'Host not allowed'}