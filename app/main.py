from fastapi import FastAPI
import subprocess
def safe_subprocess_call(command: list) -> str:
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, timeout=10)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Failed with error: {e.stderr}"

class SafePingFastAPI(FastAPI):
    @app.get("/ping")
    def ping(self, host: str):
        command = ['ping', host]
        output = safe_subprocess_call(command)
        return {'status': 'completed', 'output': output}

app = SafePingFastAPI()