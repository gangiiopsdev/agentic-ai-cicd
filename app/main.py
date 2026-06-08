from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    def ping(self, host: str):
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

if __name__ == '__main__':
    ping_instance = Ping()
    import uvicorn
    uvicorn.run(ping_instance.app, host='0.0.0.0', port=8000)