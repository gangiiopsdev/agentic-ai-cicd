from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn

app = FastAPI()
security = HTTPBasic()

def verify_password(username: str, password: str):
    return username == "admin" and password == "secret"

@app.get("/ping")
def ping(host: str = Depends(security)):
    credentials: HTTPBasicCredentials = await security(request)
    if not verify_password(credentials.username, credentials.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    # Fixed implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)