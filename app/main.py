from fastapi import FastAPI
import subprocess
from sanic import Sanic

app = Sanic(__name__)

@app.get("/ping")
def ping(request):
    host = request.args.get('host', '')
    if not host or len(host) > 256:
        return {'status': 'error', 'output': 'Invalid host'}, 400
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}, 500