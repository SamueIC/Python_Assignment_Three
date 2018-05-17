from Interpreter.database_handler import DatabaseHandler
from Interpreter.filehandler import FileHandler
from os import path
from Interpreter.chart import Graph
import doctest


# Wesley
class Controller:
    def __init__(self):
        self.db_handler = DatabaseHandler()
        self.data = None
        self.filehandler = None
        self.graph = None

    def load(self, filename):
        """
        Set the file that will create the filehandler object
        """
        if path.exists(filename):
            self.filehandler = FileHandler(filename)
            self.filehandler.set_file_type()
            return True
        else:
            return False

    def validate(self):
        """
        Read selected file
        """
        # James' changes (13/03)
        result = self.filehandler.read()
        self.data = result
        print("")
        print(result)

    def set_local(self, connection):
        """
        Set the local database with a specified name
        :param connection:
        :return:
        """
        self.db_handler.set_local(connection)
        self.db_handler.insert_local_dict(self.data)

    def set_remote(self, host, user, password, db):
        """
        Set the remote database
        :param host, user, password, db:
        :return:
        """
        self.db_handler.set_remote(host, user, password, db)
        self.db_handler.insert_remote_dict(self.data)

    def set_graph(self, graph_type, filename):
        print(graph_type)
        print(filename)
        self.graph = Graph()
        data = self.data
        self.graph.set_data(data, graph_type, filename)

    def get_local(self):
        self.data = self.db_handler.get_local()

    def get_remote(self):
        self.data = self.db_handler.get_remote()

    def set_criteria(self, criteria_1, criteria_2=None):
        self.graph.set_criteria(criteria_1, criteria_2)

    def set_keys(self, key_1, key_2=None):
        self.graph.set_keys(key_1, key_2)

    def draw(self, x, y, title):
        self.graph.draw(x, y, title)

    def check_data(self):
        if self.data is not None:
            return True
        return False
