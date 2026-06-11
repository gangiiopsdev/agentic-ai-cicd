from fastapi import FastAPI
import subprocess
from fastapi.exceptions import HTTPException

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail=f'Ping failed: {e.stderr}')