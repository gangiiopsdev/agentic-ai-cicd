from fastapi import FastAPI
import subprocess
gt

app = FastAPI()

gt
@app.get("/ping")
def ping(host: str):
    # Safe implementation
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}
gt