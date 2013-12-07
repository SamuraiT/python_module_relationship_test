from world.world import World

class Hello(object):
    def __str__(self):
        return 'Hello'
    def hello_world(self):
        return str(self) + str(World())
if __name__ == '__main__':
    hi = Hello()
    print hi.hello_world()

    
