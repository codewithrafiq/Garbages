import uvicorn


if __name__=="__main__":
    uvicorn.run("project:app",port=8077, log_level="info", reload=True) 