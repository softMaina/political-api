from flask import Flask, abort

OFFICES = []
class Office(object):
    def __init__(self):
        self.office = OFFICES
    
    
    def add_office(self,name,office_type):
        office={
            'id':len(self.office)+1,
            'name':name,
            'office_type':office_type
        }
        self.office.append(office)

    def get_offices(self):
        return self.office  
        
    
    def get_specific_office(self, office_id):
        office = [task for task in self.office if task['id'] == office_id]
        return office       

    def update_office(self,office_id,name,office_type):
        
        office = [task for task in self.office if task['id'] == office_id]
        
        if len(office) == 0:
            return abort(400)
        office[0]['name'] = name
        office[0]['office_type']= office_type