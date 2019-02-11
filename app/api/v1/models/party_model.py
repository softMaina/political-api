from flask import Flask, abort

PARTIES = []
class Party(object):
    def __init__(self):
        self.party = PARTIES
    
    # create party
    def add_party(self,name,hqaddress,logoUrl):
        party={
            'id':len(self.party)+1,
            'NAME':name,
            'slogan':hqaddress,
            'logoUrl':logoUrl
        }
        self.party.append(party)

    def get_parties(self):
        return self.party
        
    def get_specific_party(self, party_id):
         party = [task for task in self.party if task['id'] == party_id]
         return self.party        

    def update_party(self,party_id,name,hqaddress,logoUrl):
        
        party = [task for task in self.party if task['id'] == party_id]
        
        if len(party) == 0:
            return abort(400)
        party[0]['name'] = name
        party[0]['hqaddress']= hqaddress
        party[0]['logoUrl']=logoUrl  


    def delete_party(self,party_id):

        party = [task for task in self.party if task['id'] == party_id]

        if len(party) == 0:
            abort(400)
        self.party.remove(party[0])