import peewee
from db_init.models_tables import Contracts
from utils import status_message, input_fild


#Serch one contract
def serch_contract(status:str=None) -> peewee.Model:
    try:        
        contract_id = int(input_fild(f'{status if status else "-"} contract id'))
        contract = Contracts.select().where(Contracts.contract_id==contract_id)
        
        if status and contract:
            contract = contract.where(Contracts.status_contract==status)
            
        if contract:
            return contract.get()        
    except peewee.OperationalError:        
        status_message('Database connection error')
        
        
#Serch all contracts
def serch_contracts(status:str=None) -> list:
    try:        
        contracts = Contracts.select()
        if status:
            contracts = contracts.where(Contracts.status_contract==status)
            
        return [v for v in contracts.dicts()]
    except peewee.OperationalError:        
        status_message('Database connection error')              

