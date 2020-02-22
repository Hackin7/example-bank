class ExampleStructure:
    def __init__(self,name,topics,description):
        self.name = name
        self.topics = topics
        self.description = description
    def matchSearch(self,search):
        if search=="":
            return True
        else:
            if search in self.name or\
                search in self.topics or\
                search in self.description:
                return True
            else:
                return False
    def __str__(self):
        return f"{self.name}: about {self.topics}"
