from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        ip_address = host.split('@')[1]
        # Use check_output instead of call with shell=True
        output = subprocess.check_output(['ping', '-c', '4', ip_address], timeout=5)
        return output.decode()
    except (subprocess.CalledProcessError, IndexError) as e:
        return str(e)

class App(FastAPI):
    @app.get("/")
    def home(self):
        return {"message": "Agentic Self-Healing Pipeline"}

    @app.get("/ping")
    def ping(self, host: str):
        result = safe_ping(host)
        return {"status": "completed", "result": result}