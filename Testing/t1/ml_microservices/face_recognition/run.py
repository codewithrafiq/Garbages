from imp import reload
import uvicorn


if __name__ == "__main__":
    uvicorn.run("project:app", host="0.0.0.0", port=8889, log_level="info",reload=True)