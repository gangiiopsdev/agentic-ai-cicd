from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
def safe_ping(host: str):
    try:
        # Sanitize input to prevent command injection
        if not host.isalnum():
            raise ValueError('Invalid host name')
        args = ['ping', host]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={'error': e.stderr.decode('utf-8')})
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    response = safe_ping(host)
    return response