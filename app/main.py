from fastapi import FastAPI
import re
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Validate the host input to prevent injection attacks
        raise ValueError('Invalid host name')
    args = ['ping', '-c', '1', host]  # Limit the number of pings and use -c for compatibility
    subprocess.run(args, check=True, shell=False)  # Ensure shell=False to prevent shell injection
    return {'status': 'completed'}