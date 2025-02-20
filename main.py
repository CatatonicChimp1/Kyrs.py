import uvicorn
from __init__ import CONFIG

if __name__ == "__main__":
    uvicorn.run("api:app", host=CONFIG["host"], port=CONFIG["port"], reload=True)
