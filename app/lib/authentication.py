import string
from db import session
from model.authentication import AuthenticationTable,Authentication


def simple_authentication(key_code:string):
    authentication = session.query(AuthenticationTable).\
        filter(AuthenticationTable.key_code == key_code).first()
    if(authentication):
        return authentication.id
    else:
        return False
