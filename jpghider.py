class Hider:
    def __init__(self, path, endstring = None, format=None) -> None:
        self.path = path
        dict = {"jpg":"FFD9", "png":"49454E44AE426082"}
        if format is not None:
            self.string = dict[format]
            self.length = len(dict[format])//2
        else:
            self.string = endstring
            self.length = len(endstring)//2
    
    def appendbyte(self, bytes):
        with open(self.path, 'ab') as file:
            file.write(bytes)
            
    def appendfile(self, name):
        with open(name, 'rb') as f:
            bytes = f.read()
        with open(self.path, 'ab') as file:
            file.write(bytes)

    def showoutput(self):
        with open(self.path, 'rb') as file:
            content = file.read()
            index = content.index(bytes.fromhex(self.string))
            file.seek(index+self.length)
            byte = file.read()
            return byte

    def makefile(self, name):
        with open(name, 'wb') as f:
            f.write(self.showoutput())

    def delete(self):
        with open(self.path, 'rb') as file:
            content = file.read()
            index = content.index(bytes.fromhex(self.string))
            content = content[:index+self.length]
        with open(self.path, 'wb') as f:
            f.write(content)
    
    def showcontent(self):
        with open(self.path, 'rb') as file:
            byte = file.read()
            print(byte)
            return byte
    
