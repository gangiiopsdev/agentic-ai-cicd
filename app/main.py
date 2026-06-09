from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum() or len(v) > 255:
            raise ValueError('Invalid host input')
        return v

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Use a safer method to validate and sanitize user input before constructing the command
    if request.host.isalnum() and len(request.host) <= 255:
        subprocess.run(['ping', request.host], check=True, shell=False)