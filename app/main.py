from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
def escape_command(command):
    return [arg.replace(';', '').replace('&', '') for arg in command]
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(escape_command(['ping', host]), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return JSONResponse(content={'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode() if result.stderr else None}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)