from fastapi import FastAPI
import subprocess
global host_list
host_list = ['google.com', 'example.com']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in host_list:
        return {'error': 'Host not allowed'}
    # Secure implementation using subprocess.run with shell=False and proper input validation
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}