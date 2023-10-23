import os
import uvicorn
from dotenv import load_dotenv
from apps.__init__ import app

## load enviornment variables
load_dotenv()


if __name__ == '__main__':
    uvicorn.run("asgi:app",
        host=os.environ.get("SERVER_HOST"),
        port=int(os.environ.get("SERVER_PORT")),
        reload=True)