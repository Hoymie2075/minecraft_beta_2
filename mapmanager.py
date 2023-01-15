# напиши здесь код создания и управления картой
import pickle

class Mapmanager():
    def __init__(self):
        self.model = 'block'
        self.texture = 'dirt.png'
        self.color = (0.2, 0.2, 0.35, 1)
        self.startNew()
        self.addBlock((0, 10, 0))

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
        self.block.setTag("at", str(position))

    def delBlock(self, pos):
        blocks = self.land.findAllMatches("=at=" + str(pos))
        for block in blocks:
            block.removeNode()


    def  loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block  = self.addBlock((x, y, z0))
                    x += 1
                y += 1
        return x, y
    
    def clear(self):
        self.land.removeNode()
        self.startNew()

    def saveMap(self):
        blocks = self.land.getChildren()
        with open('my_map.dat', 'wb') as fout:
            pickle.dump(len(blocks), fout)
            for block in blocks:
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, fout)

    def loadMap(self):
        self.clear()
        with open('my_map.dat', 'rb') as fin:
            length = pickle.load(fin)
            for i in range(length):
                pos = pickle.load(fin)
                self.addBlock(pos)