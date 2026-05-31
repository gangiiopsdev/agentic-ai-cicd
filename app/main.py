from fastapi import FastAPI
import subprocess
from sanic.response import text

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return text('Invalid input', status=400)
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)