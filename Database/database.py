from exampleStructure import ExampleStructure
import sqlite3

class Database:
    def __init__(self):
        self.dbFile = './Database/examples.db'
        try: self.setupDB()
        except Exception as e:print(e)
        
    def setupDB(self):
        with sqlite3.connect(self.dbFile) as conn:
            conn.execute('''
            CREATE TABLE examples
             (ID INT PRIMARY KEY  NOT NULL ,
             name           TEXT    NOT NULL,
             topic          TEXT    NOT NULL,
             description    TEXT    NOT NULL);
             ''')
    def getID(self,exampleId):
        exampleId = str(exampleId)
        with sqlite3.connect(self.dbFile) as conn:
            cursor = conn.execute("SELECT * from examples WHERE ID=?",(exampleId))
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

db = Database()
