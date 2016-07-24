import itertools, random

from GameSetup import setup

class Hex(object):
    def __init__(self, resource, value=(0, 0, 0), location=(0,0)):
        self.resource = resource
        self.value = value
        self.location = location

    def __str__(self):
                return 'A "%s" hex, with number: %s, and value %s is at position: %s' % (self.resource, self.number, self.value, self.location)
    def getResource(self):
        return self.resource
    def getValue(self):
        return self.value
    def getLocation(self):
        return self.location

if __name__=='__main__':

    setup(Hex, itertools, random)
    print "Setup Complete!"