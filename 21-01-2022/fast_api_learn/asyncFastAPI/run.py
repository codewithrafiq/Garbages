import uvicorn
from project.db import metadata
from project.db import engine

if __name__ == "__main__":
    metadata.create_all(engine)
    uvicorn.run("project:app", host="0.0.0.0", port=8000, reload=True,debug=True)