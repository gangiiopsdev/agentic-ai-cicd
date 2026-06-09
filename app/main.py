from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host):
    try:
        args = ['ping'] + shlex.split(host)
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class PingResponse(BaseModel):
    status: str
    message: Union[str, None] = None
    output: Union[str, None] = None

@app.get("/ping")
def ping(host: str):
    output = secure_ping(host)
    if isinstance(output, str) and 'Command not found' in output:
        return PingResponse(status='failed', message='Invalid command', output=None)
    else:
        return PingResponse(status='completed', message='Success', output=output)