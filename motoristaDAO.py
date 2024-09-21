from pymongo import MongoClient
from bson.objectid import ObjectId


class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, nota: int):
        try:
            motorista = {
                "nota": nota,
                "corridas": []  # Inicialmente, sem corridas
            }
            res = self.db.collection.insert_one(motorista)
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating motorista: {e}")
            return None

    def read_motorista_by_id(self, motorista_id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(motorista_id)})
            if res:
                print(f"Motorista found: {res}")
            else:
                print("Motorista not found.")
            return res
        except Exception as e:
            print(f"An error occurred while reading motorista: {e}")
            return None

    def update_motorista(self, motorista_id: str, nova_nota: int):
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(motorista_id)},
                {"$set": {"nota": nova_nota}}
            )
            print(f"Motorista updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating motorista: {e}")
            return None

    def delete_motorista(self, motorista_id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(motorista_id)})
            print(f"Motorista deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorista: {e}")
            return None

    def add_corrida(self, motorista_id: str, corrida: dict):
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(motorista_id)},
                {"$push": {"corridas": corrida}}
            )
            print(f"Corrida added to motorista: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while adding corrida: {e}")
            return None