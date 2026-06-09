from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.exceptions import HTTPException
from pydantic import validator

app = FastAPI()
bearer_scheme = HTTPBearer()

class HostModel(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
        if not pattern.match(v): raise ValueError('Invalid host parameter')
        return v

@app.get("/ping")
def ping(host_model: HostModel = Depends()):
    args = ['ping', host_model.host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "result": result.stdout}

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.scheme.lower() != 'bearer':
        raise HTTPException(status_code=403, detail='Invalid authentication scheme')
    # Add token verification logic here