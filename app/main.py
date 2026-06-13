from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
generate_ping_command = lambda host: f"ping {host}"

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    try:
        result = subprocess.run(generate_ping_command(request.host).split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "stderr": e.stderr.decode()}