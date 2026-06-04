from fastapi import FastAPI
import subprocess
import shlex

class App:
    def __init__(self):
        self.app = FastAPI()

    def safe_ping(self, host: str):
        if not host.isalnum():
            raise ValueError('Invalid host name')
        command = ['ping', shlex.quote(host)]
        subprocess.run(command, shell=False, check=True)

    @app.get("/ping")
    def ping(self, host: str):
        self.safe_ping(host)
        return {"status": "completed"}

if __name__ == '__main__':
    app_instance = App()
    import uvicorn
    uvicorn.run(app_instance.app, host='127.0.0.1', port=8000)