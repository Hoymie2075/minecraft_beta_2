

class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.6)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
        
    

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn == True:
            self.cameraUp()
        else:
            self.cameraBind()

    def accept_events(self):
        base.accept('c', self.changeView)
        base.accept('q', self.turn_left)
        base.accept('q'+'-repeat', self.turn_left)

        base.accept('e', self.turn_right)
        base.accept('e'+'-repeat', self.turn_right)

        base.accept('w', self.forward)
        base.accept('w'+'-repeat', self.forward)

        base.accept('s', self.back)
        base.accept('s'+'-repeat', self.back)

        base.accept('a', self.left)
        base.accept('a'+'-repeat', self.left)

        base.accept('d', self.right)
        base.accept('d'+'-repeat', self.right)

        base.accept('space', self.up)
        base.accept('space'+'-repeat', self.up)

        base.accept('shift', self.down)
        base.accept('shift'+'-repeat', self.down)

        base.accept('mouse1', self.build)

        base.accept('mouse3', self.destroy)

        base.accept( 'k',  self.land.saveMap )

        base.accept( 'l',  self.land.loadMap )
    
    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def forward(self):
        angle = (self.hero.getH()) % 360
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def back(self):
        angle = (self.hero.getH() + 180) % 360
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def left(self):
        angle = (self.hero.getH() + 90) % 360
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def right(self):
        angle = (self.hero.getH() + 270) % 360
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def up(self):
        z = self.hero.getZ()
        self.hero.setZ(z + 1)

    def down(self):
        z = self.hero.getZ()
        self.hero.setZ(z - 1)

    def build(self):
        angle = (self.hero.getH()) % 360
        pos = self.look_at(angle)
        self.land.addBlock(pos)

    def destroy(self):
        angle = (self.hero.getH()) % 360
        pos = self.look_at(angle)
        self.land.delBlock(pos)

    def look_at(self, angle):
        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from

    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return(0, -1)

    
        