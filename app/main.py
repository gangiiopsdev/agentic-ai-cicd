from fastapi import FastAPI
import subprocess
class PingHost:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    def ping(self, host: str):
        # Safe implementation using subprocess.run with shell=False and args
        try:
            subprocess.run(['ping', host], check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': f'Ping failed with error: {e}'}

if __name__ == "__main__":
    ping_host = PingHost()
    import uvicorn
    uvicorn.run(ping_host.app, host='0.0.0.0', port=8000)