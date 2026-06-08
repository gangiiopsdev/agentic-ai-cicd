from fastapi import FastAPI
import subprocess
class PingResponse(BaseModel):
    status: str
    output: str
app = FastAPI()
def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ('.', '-', '_'))
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, shell=False)
        return PingResponse(status='completed', output=result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}, 500