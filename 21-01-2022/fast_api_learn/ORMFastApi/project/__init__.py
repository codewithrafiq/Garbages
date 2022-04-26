from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI() 



register_tortoise(
    app,
    db_url="sqlite://test.db",
    modules={"models": ["project.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)



from project import routes


app.include_router(routes.route)