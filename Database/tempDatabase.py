from exampleStructure import ExampleStructure

class Database:
    def __init__(self):
        self.data = [ExampleStructure("Malala Yousafazai",["Education"],"She was in <code>Swat Valley</code>")]
    def getID(self,exampleId):
        return self.data[exampleId]
    def search(self,query):
        result = []
        for i in range(len(self.data)):
            if self.data[i].matchSearch(query):
                result.append((i,self.data[i]))
        return result
        
db = Database()
