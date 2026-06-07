from fastapi import FastAPI
class PingRequest(BaseModel):
    host: str
async def ping(host: PingRequest):
    cmd = ['ping', host.host]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}