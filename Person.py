from Address import Address
class Person :
    
    def __init__(self,firstName,lastName,phoneNumber,dateOfBirth):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.dateOfBirth = dateOfBirth
        self.address = []
    
    
    def addAddress(self,address) :
        if isinstance(address,Address) :
            self.address.append(address)
        elif isinstance(address,list):
            for entry in address :
                if not isinstance(entry,Address):
                    pass
                   # raise Error('Invalid Address')
            self.address = address
        else :
            pass
            #raise Error('Invalid Address')
    
    def covert_address_to_string(self):
        if len(self.address) != 0 :
            str_address = ''
            count = 0
            for address in self.address :
                mystr = address.country + ' ' + address.city + ' ' + address.street + ' ' + address.postal + ';'
                
                str_address += mystr
                count += 1
            
            return str_address
    
    
    