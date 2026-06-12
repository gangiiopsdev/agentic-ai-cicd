from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.exceptions import HTTPException

app = FastAPI()
security = HTTPBasic()

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(security)):
    host = credentials.username  # Assuming username contains the host to ping
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return HTTPException(status_code=400, detail=e.stderr)