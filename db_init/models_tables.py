import peewee #include module 
from datetime import date
from db_init.db_connection import db #include database 

#include Base Model
class BaseModel(peewee.Model):    
    class Meta:
        database = db
        
#include Contracts Model
class Contracts(BaseModel):    
    contract_id = peewee.PrimaryKeyField(null=False)
    contract_name = peewee.CharField(null=False, unique=True, max_length=200)
    signature_date = peewee.DateField(null=True)
    status_contract = peewee.CharField(default='Draft')
    project_id = peewee.CharField(null=True)
    date_of_creation = peewee.DateField(default=date.today())
    
    class Meta:
        order_by = ('contract_id',)
    
        
#include Projects Model        
class Projects(BaseModel):
    project_id = peewee.PrimaryKeyField(null=False)
    project_name = peewee.CharField(null=False, unique=True, max_length=200)
    contract = peewee.ForeignKeyField(Contracts,                                         
                                        related_name="projects",
                                        to_field='contract_id',
                                        on_delete='SET NULL',
                                        on_update='CASCADE',
                                        null=True,
                                    )
    date_of_creation = peewee.DateField(default=date.today())   
    
    class Meta:
        order_by = ('project_id',)

