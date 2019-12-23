def SaveFile(path):
        file = open(path, 'w')
        file.write('a')

SaveFile('abc.txt')