from fastapi import FastAPI
import subprocess
class HostValidator:
    @staticmethod
    def validate(host: str):
        return host.isalnum()

app = FastAPI()

@app.get("/ping")
def ping(host: str = Depends(HostValidator.validate)):
    subprocess.run(['ping', f'-c 1 {host}'], check=True, stdout=subprocess.PIPE)
    return {'status': 'completed'}