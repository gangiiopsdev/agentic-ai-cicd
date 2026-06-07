from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class SanitizedString(BaseModel):
    value: str = None

    @validator('value')
    def validate_value(cls, v):
        return ''.join(char for char in v if char.isalnum() or char in '-:.')

app = FastAPI()

@app.get("/ping")
def ping(host: SanitizedString):
    sanitized_host = host.value.strip()
    if not sanitized_host:
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(['ping', f'-c 1 {sanitized_host}'], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}