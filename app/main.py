from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return result.stdout

class App:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    def ping(self, host: str):
        output = safe_ping(host)
        return {"status": "completed", "output": output}

if __name__ == '__main__':
    app_instance = App()
    import uvicorn
    # Use a specific IP instead of 0.0.0.0 to limit exposure
    uvicorn.run(app_instance.app, host="127.0.0.1", port=8000)