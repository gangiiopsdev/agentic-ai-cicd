from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Safe implementation using subprocess.Popen
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class PingRouter:
    @staticmethod
def ping(host: str):
        return execute_ping(host)
app = FastAPI()

@app.get("/ping")
def ping_controller(host: str):
    response = PingRouter.ping(host)
    return {'status': 'completed', 'response': response}