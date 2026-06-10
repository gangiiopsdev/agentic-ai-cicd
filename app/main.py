from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}, 403

    args = ['ping', '-c', '1', host]  # Limit the number of pings for security
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return jsonable_encoder({'status': 'completed', 'output': result.stdout})