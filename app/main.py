from fastapi import FastAPI
import shlex
tfrom pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    validated_host = shlex.quote(request.host)
    result = subprocess.run(['ping', '-c', '1'] + shlex.split(validated_host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}