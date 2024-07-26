from quart import Blueprint, jsonify, request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
import models.user_model as user_model
import db.db_config as db_config
import utils.get_data as get_data

User = user_model.User
get_db = db_config.get_db # Obtener la sesion de la base de datos

# Ruta de usuario
NAME_ROUTE = 'user'

user_bp = Blueprint(NAME_ROUTE, __name__)

@user_bp.route('/', methods=['GET'])
async def get_users():
  try: 
    async for db in get_db():
      result = await db.execute(select(User))
      users = result.scalars().all()
      return jsonify([get_data.as_dict(user) for user in users])
  except Exception as e:
    return jsonify({"error": str(e)}), 500

@user_bp.route('/<int:user_id>', methods=['GET'])
async def get_user_by_id(user_id: int):
  try:
    async for db in get_db():
      result = await db.execute(select(User).where(User.id == user_id))
      user = result.scalars().first()

      if not user:
        return jsonify({"error": "User not found"}), 404

      return jsonify(get_data.as_dict(user))
  except Exception as e:
    return jsonify({"error": str(e)}), 500

@user_bp.route('/', methods=['POST'])
async def create_user():
  try:
    data = await request.get_json()

    if not isinstance(data, dict):
      raise ValueError("Invalid data format, expected a dictionary")
    
    async for db in get_db():
      user = User(**data)
      db.add(user)
      await db.commit()

      return jsonify(get_data.as_dict(user)), 201

  except Exception as e:
    return jsonify({"error": str(e)}), 500
  
@user_bp.route('/<int:user_id>', methods=['PUT'])
async def update_user(user_id: int):
  try:
    data = await request.get_json()

    if not isinstance(data, dict):
      raise ValueError("Invalid data format, expected a dictionary")
    
    async for db in get_db():
      result = await db.execute(select(User).where(User.id == user_id))
      user = result.scalars().first()

      if not user:
        return jsonify({"error": "User not found"}), 404

      for key, value in data.items():
        setattr(user, key, value)
      
      await db.commit()

      return jsonify(get_data.as_dict(user))
  except Exception as e:
    return jsonify({"error": str(e)}), 500

@user_bp.route('/<int:user_id>', methods=['DELETE'])
async def delete_user(user_id: int):
  try:
    async for db in get_db():
      result = await db.execute(select(User).where(User.id == user_id))
      user = result.scalars().first()

      if not user:
        return jsonify({"error": "User not found"}), 404

      await db.delete(user)
      await db.commit()

      return jsonify({"message": "User deleted successfully"})
  except Exception as e:
    return jsonify({"error": str(e)}), 500
  
