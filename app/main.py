from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    # Implement token verification logic here
    pass

@app.get("/ping")
def ping_handler(host: str):
    await verify_token()
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}