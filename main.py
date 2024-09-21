from database import Database
from motoristaDAO import MotoristaDAO
from cli import MotoristaCLI

db = Database(database="Avaliativo", collection="motoristas")
motorista_dao = MotoristaDAO(database=db)

motorista_cli = MotoristaCLI(motorista_dao)
motorista_cli.run()
