from PIL import Image as PILImage

class Image:
    def __init__(self):
        self._name = ""
        self._img = PILImage.new("RGB",(0,0))
        self._type = self._img.mode
        self._data = self._img.load()

    def show(self):
        self._img.show()

    def __getitem__(self,idx):
        return self._data[idx[0],idx[1]]

    def __setitem__(self,idx,val):
        self._data[idx[0],idx[1]] = val

    def size(self):
        return self._img.size

    def pixels(self):
        return self._img.size[0]*self._img.size[1]

    def name(self):
        return self._name

    def img_type(self):
        return self._type

    def open(self,name):
        self._name = name
        self._img = PILImage.open(name)
        self._type = self._img.mode
        self._data = self._img.load()

    def createEmpty(self,dims):
        self._name = "custom"
        self._img = PILImage.new("RGB",dims)
        self._type = self._img.mode
        self._data = self._img.load()


def open(name):
    img = Image()
    img.open(name)
    return img

def empty(dims):
    img = Image()
    img.createEmpty(dims)
    return img
