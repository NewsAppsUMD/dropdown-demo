from peewee import *
import os

# Define the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'election_results.db')
database = SqliteDatabase(db_path)

class BaseModel(Model):
    """Base model class that specifies which database to use"""
    class Meta:
        database = database

class ElectionResult(BaseModel):
    """Model for election results by jurisdiction"""
    jurisdiction = CharField(primary_key=True)
    harris = IntegerField()
    trump = IntegerField()
    oliver = IntegerField()
    stein = IntegerField()
    kennedy = IntegerField()
    others = IntegerField()
    total = IntegerField()
    
    class Meta:
        table_name = 'election_results'

    def to_dict(self):
        """Convert model instance to dictionary"""
        return {
            'jurisdiction': self.jurisdiction,
            'harris': self.harris,
            'trump': self.trump,
            'oliver': self.oliver,
            'stein': self.stein,
            'kennedy': self.kennedy,
            'others': self.others,
            'total': self.total,
            'percentages': {
                'harris': round(self.harris / self.total * 100, 2),
                'trump': round(self.trump / self.total * 100, 2),
                'oliver': round(self.oliver / self.total * 100, 2),
                'stein': round(self.stein / self.total * 100, 2),
                'kennedy': round(self.kennedy / self.total * 100, 2),
                'others': round(self.others / self.total * 100, 2)
            }
        }

# Connect to the database
def initialize_db():
    database.connect()
    database.create_tables([ElectionResult], safe=True)
    database.close()

if __name__ == '__main__':
    initialize_db()