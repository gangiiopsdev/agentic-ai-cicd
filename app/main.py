from fastapi import FastAPI
import subprocess
call = subprocess.run(['ping', host], check=False)