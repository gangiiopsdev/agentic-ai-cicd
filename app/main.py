from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Secure implementation using check_output
        args = ['ping', host]
        try:
            output = subprocess.check_output(args, stderr=subprocess.STDOUT)
            return {"status": "completed", "output": output.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "error": e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return SafeSubprocess.ping(host)