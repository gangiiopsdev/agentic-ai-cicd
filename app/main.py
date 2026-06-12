from fastapi import FastAPI
import subprocess
from fastapi.middleware.cors import CORSMiddleware

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', self.host]
        process = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await process.communicate()
        return output.decode('utf-8')
global app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/ping")
def ping(host: str):
    if not host.isdigit():  # Basic validation to prevent injection
        return {"status": "error", "message": "Invalid input"}
    try:
        command = PingCommand(host)
        result = await command.execute()
        return {"status": "completed", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}