from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host or ' ' in host:
        return False
    args = ['ping', '-c', '1', host]  # Limit the number of pings to mitigate risks
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode(), result.stderr.decode()

class FastAPIPing:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    async def ping(self, host: str):  
        if not host or ' ' in host:
            return {'error': 'Invalid input'}
        status, output = safe_ping(host)
        if status:
            return {'status': 'completed', 'output': output}
        else:
            return {'error': 'Invalid input'}

# Usage
if __name__ == "__main__":
    app_instance = FastAPIPing()
    import uvicorn
    uvicorn.run(app_instance.app, host="127.0.0.1", port=8000)