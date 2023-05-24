
class Address :
    
    def __init__(self,id,country,city,street,postal):
        self.id = id
        self.country = country
        self.city = city
        self.street = street
        self.postal = postal
        
    def __repr__(self) -> str:
        return f"Address '{self.id}' -> {self.country}, {self.city} {self.street} {self.postal}"
        
        