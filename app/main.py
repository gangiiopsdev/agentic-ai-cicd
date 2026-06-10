from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return JSONResponse(content={'error': 'Invalid hostname'}, status_code=400)

    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        return JSONResponse(content={'result': 'Ping failed'}, status_code=500)
    else:
        return JSONResponse(content={'result': 'Ping successful'})