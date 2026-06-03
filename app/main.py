from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    try:
        sanitized_host = sanitize_input(request.host)
        result = subprocess.run(['ping', '-c', '1', f'{sanitized_host}'], capture_output=True, text=True, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}
    return {"status": "completed", "output": result.stdout}