"""Search for particular file in given directory"""

class search:

    def __init__(self, args):
        self.args = args


    def search_file(self, file_name, path):
        from file import files

        obj = files()
        temp = obj.show(path = path)

        result = [x for x in temp if x == file_name]
        return '\t'.join(result)


    def parse(self):
        if len(self.args) != 3:
            return "command length invalid"

        return (self.search_file(self.args[1], self.args[2]))
        


