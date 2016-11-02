class CaffeVectorsIterator():
    def __init__(self, file_path):
        self.file = open(file_path, 'rb')

    def next(self):
        try:
            # (id: int, vector: tuple of float)
            lineA=self.file.next()
            lineB=self.file.next()
            print(lineA)
            print(lineB)
            return (int(lineA.split(' ')[2]), tuple([float(num) for num in lineB.split(' ')]))
        except StopIteration:
            self.file.close()
            raise StopIteration

class CaffeVectorsIterable():
    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self):
        return CaffeVectorsIterator(self.file_path)
