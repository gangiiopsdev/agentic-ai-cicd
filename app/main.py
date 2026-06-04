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
        if subprocess.call(['ping', '-c', '1', f'{sanitized_host}'], capture_output=True, text=True) == 0:
            return {"status": "completed", "output": result.stdout}
        else:
            return {"status": "error", "output": "Ping failed"}
    except Exception as e:
        return {"status": "error", "output": str(e)}