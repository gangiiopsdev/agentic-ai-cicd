from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
@app.get("/ping")
def ping(request: PingRequest):
    try:
        # Validate the input to ensure it does not contain potentially harmful characters
        if '&&' in request.host or '|' in request.host or ';' in request.host:
            raise ValueError("Invalid input detected")
        output = subprocess.run(["ping", request.host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}