from fastapi import FastAPI
import subprocess
class HostValidator:
    @staticmethod
    def validate(host: str):
        return host.isalnum()

app = FastAPI()

@app.get("/ping")
def ping(host: str = Depends(HostValidator.validate)):
    try:
        result = subprocess.run(['ping', f'-c 1 {host}'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}