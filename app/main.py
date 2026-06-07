from fastapi import FastAPI
import subprocess

app = FastAPI()

async def run_ping(host):
    # Safer implementation using Popen and list of args
    args = ['ping', host]
    process = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
    result = await process.communicate()
    return result[0]

@app.get("/ping")
def ping(host: str):
    try:
        response = run_ping(host)
        return {'status': 'completed', 'response': response}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}