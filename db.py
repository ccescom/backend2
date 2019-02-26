import sqlite3


class Database:

    def __init__(self, db_path):

        self.db_path = db_path
        self.db = sqlite3.connect(db_path, check_same_thread = False)

        self.cursor = self.db.cursor()

    def insert(self, query, parms):

        if parms == None :
            result = self.cursor.execute(query)
            self.db.commit()
            print(result)
            return

        result = self.cursor.execute(query, parms)
        self.db.commit()


    def select(self, query, parms):

        result = None

        if parms == None :

            result = self.cursor.execute(query)
            res = []
            for row in result:
                d = {}
                for idx, col in enumerate(self.cursor.description):
                    d[col[0]] = row[idx]
                res.append(d)
            return res

        result = self.cursor.execute(query, parms)
        res = []
        for row in result:
           d = {}
           for idx, col in enumerate(self.cursor.description):
              d[col[0]] = row[idx]
           res.append(d)

        return res

