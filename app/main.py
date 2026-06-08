from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = ''.join(filter(str.isalnum, host))
    args = ['ping', safe_host]
    result = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()
    return {'status': 'completed'}