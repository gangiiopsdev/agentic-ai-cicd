from fastapi import FastAPI
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    try:
        response = subprocess.run(['ping', '-c 1', shlex.quote(request.host)], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': response.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except TimeoutExpired as e:
        return {'status': 'error', 'message': str(e)}