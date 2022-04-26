import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "project:demo",
        host="0.0.0.0",
        port=8000,
    )
