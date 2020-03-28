from exampleStructure import ExampleStructure
import sqlite3

class Database:
    def __init__(self,dbfile='./examples.db'):
        self.dbFile = dbfile
        try: self.setupDB()
        except Exception as e:print(e)
        
    def setupDB(self):
        with sqlite3.connect(self.dbFile) as conn:
            conn.execute('''
            CREATE TABLE examples
             (ID            INTEGER  PRIMARY KEY AUTOINCREMENT,
             name           TEXT    NOT NULL,
             topic          TEXT    NOT NULL,
             description    TEXT    NOT NULL);
             ''')
             
    def getID(self,exampleId):
        exampleId = str(exampleId)
        with sqlite3.connect(self.dbFile) as conn:
            cursor = conn.execute("SELECT * from examples WHERE ID=?",(exampleId,))
            row = cursor.fetchone()
            return ExampleStructure(row[1],row[2],row[3])
        
    def search(self,query):
        result = []
        query = "%"+query+"%"
        with sqlite3.connect(self.dbFile) as conn:
            cursor = conn.execute("""SELECT * from examples
                                    WHERE name LIKE ?
                                        OR topic LIKE ?
                                        OR description LIKE ?
                                    ;""",
                                (query,query,query))
            for row in cursor:
                result.append((row[0],ExampleStructure(row[1],row[2],row[3])))
        return result
        
    def reset(self):
        with sqlite3.connect(self.dbFile) as conn:
            conn.execute('DROP TABLE examples')
        self.setupDB()
    
    def insertExample(self,data):
        '''
        data: A tuple of the name,topic,description
        '''
        with sqlite3.connect(self.dbFile) as conn:
            conn.execute('INSERT INTO examples(name,topic,description) VALUES(?,?,?)',tuple(data))
            conn.commit()
    
    def report(self,size=-1):
        with sqlite3.connect(self.dbFile) as conn:
            cursor = conn.execute("SELECT * from examples;")
            ## Output ###############################
            output = ""
            # Header
            header = ["ID","Name","Topic","Description"]
            for i in header:
                output+=f"{i:<20}"
            output+="\n"
            for row in cursor:
                for i in row:
                    j = str(i).replace('\n ','')
                    output += f"{j:<20}"   
                output+="\n"
                size-=1
                if size==0:break
        print(output)
if __name__=='__main__':
    db = Database()
    print("Report\n")
    db.report(5)
