from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.run instead of subprocess.call
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
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
    uvicorn.run(app_instance.app, host="0.0.0.0", port=8000)