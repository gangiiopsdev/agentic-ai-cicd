from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingCommand(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(ping_command: PingCommand):