"""
This file contains the function to get data from the database.
"""
def as_dict(self):
  return {col.name: getattr(self, col.name) for col in self.__table__.columns}