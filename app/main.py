from fastapi import FastAPI
import re
from sanic.response import text

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input further if necessary
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        return text('Invalid input', status=400)
    try:
        args = ['ping', '-c', '1', host]  # Limit the number of pings for security
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}