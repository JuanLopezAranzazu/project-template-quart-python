# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, Session
# from sqlalchemy.ext.declarative import declarative_base
# import config.global_config as global_config

# config = global_config.config
# database = config["db"]

# database_uri = f"mysql+pymysql://{database["user"]}:{database["password"]}@{database["host"]}:{database["port"]}/{database["name"]}"

# # Crear el motor de la base de datos
# engine = create_engine(database_uri, echo=True)

# # Crear la sesion de la base de datos
# SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=Session, future=True)

# # Crear la base de datos
# Base = declarative_base()

# # Funcion para inicializar la base de datos
# def init_db():
#   Base.metadata.create_all(bind=engine)

# # Funcion para obtener la sesion de la base de datos
# def get_db():
#   db = SessionLocal()
#   try:
#     yield db
#   finally:
#     db.close()


from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
import config.global_config as global_config
import models.base_model as base_model
from typing import AsyncGenerator

config = global_config.config
database = config["db"]
Base = base_model.Base

database_uri = f"mysql+aiomysql://{database["user"]}:{database["password"]}@{database["host"]}:{database["port"]}/{database["name"]}"

# Crear el motor de la base de datos
engine = create_async_engine(database_uri, echo=True)

# Crear la sesión de la base de datos
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession, future=True)

# Función para inicializar la base de datos
# async def init_db():
#   async with engine.begin() as conn:
#     await conn.run_sync(Base.metadata.create_all)

# # Función para obtener la sesión de la base de datos
# async def get_db() -> AsyncGenerator[AsyncSession, None]:
#   async with SessionLocal() as db:
#     try:
#       yield db
#     finally:
#       await db.close()

async def get_db():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)

  db = SessionLocal()
  try:
      yield db
  finally:
      await db.close()

