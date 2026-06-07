from fastapi import FastAPI
import subprocess
from pydantic import constr

app = FastAPI()

# Define a Pydantic model for input validation
class PingRequest(BaseModel):
    host: constr(min_length=1)

@app.get("/ping")
def ping(request: PingRequest):  # Use the validated request object
    try:
        safe_ping(request.host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

def safe_ping(host: str):
    # Secure implementation using subprocess.run with list of args
    subprocess.run(['ping', host], check=True)