from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation to avoid basic injection
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host')

@app.get(
    "/ping",
    response_model=dict,
    responses={200: {"model": dict}}
)
def ping(host: str):
    try:
        validate_host(host)
        # Use subprocess.run with shell=False for a safer approach
        result = subprocess.run(
            ["ping", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))