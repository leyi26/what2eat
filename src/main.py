from fastapi import FastAPI, Response, Depends

from src.core.config import settings
from src.lifespan import lifespan
from src.core.exception import register_exception_handlers
app = FastAPI(
    app_name= settings.app_name,
    version="1.0.0",
    description="FastAPI 项目练习",
    lifespan=lifespan
    )

register_exception_handlers(app)

# 路由引入
# @app.get("/")
# def read_root(
#     # 使用FastAPI 的依赖注入系统来获取配置实例
#     # FastAPI 会自动调用 get_settings(),由于缓存的存在,这几乎没有开销
#     settings: Settings = Depends(get_settings)
# ):
#     """
#     一个示例端点,演示如何访问配置
#     """
    
#     return {
#         "message" : f"Hello from the {settings.app_name}",
#         "database_url" : settings.database_url,
#         "jwt_secret" : settings.jwt_secret
#     }
@app.get("/health")
async def health_check(response: Response):
    response.status_code = 200
    return {"status" : "ok😲"}
