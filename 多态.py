'''
#多态栗子一：
场景：
1、定义Dog类封装方法game，普通狗狗简单玩耍；
2、定义ChaiQuan继承Dog，重写game方法，柴犬疯疯癫癫的玩耍；
3、定义Person类，封装一个和狗玩的方法，在方法内部，直接调用狗对象调用玩耍的方法；
'''
class Dog():
    def __init__(self,name):
        self.name=name
    def game(self):
        print(f'{self.name},狗狗在玩耍。')

class ChaiQuan(Dog):
    def game(self):
        print(f'{self.name},柴犬在疯疯癫癫的玩耍。')

class Person():
    def __init__(self,name):
        self.name=name
    def gameWithDog(self,dog):
        print(f'{self.name} 正在和 {dog.name} 愉快的玩耍。')
        dog.game()
'''
Person类只需要让狗对象调用game方法，而不用关心具体什么狗；
game方法是Dog父类中定义的；
在程序执行时，传入不同的狗对象参数，gameWithDog就会产生不同的执行结果；
'''
chai=ChaiQuan('小柴犬')
print(chai.name)
dog=Dog('旺财')
print(dog.name)
p=Person('zbh')
print(p.name)
p.gameWithDog(chai)
print('#'*30)
p.gameWithDog(dog)

#通过统一函数接口实现多态

class Dog():
    def sound(self):
        print('狗叫。。。')
class Cat():
    def sound(self):
        print('猫叫。。。')
def makeSound(animal):
    '''统一调用入口，不管你传进来的是什么动物，都可以调用sound()方法'''
    animal.sound()
dogobj=Dog()
catobj=Cat()
makeSound(dogobj)
makeSound(catobj)
print('************通过抽象类实现多态*********************')
#通过抽象类实现多态
'''
1、定义一个Person类，可以开车，也可以停车；
2、定义一个Car类，提供driver，stop的方法；
3、定义一个Truck，BaoMa类，继承Car类，重写driver，stop方法；
'''
class Car():
    def __init__(self,name):
        self.name=name
    def driver(self):
        '''
        抛出异常是防止通过car直接定义实例对象；
        如果car的实例调用此方法会报错，必须由子类重写才正确；
        '''
        raise NotImplementedError('Subclass must implement sbstract method.')
    def stop(self):
        raise NotImplementedError('Subclass must implement sbstract method.')
class Truck(Car):
    def driver(self):
        print(f'{self.name},Truck 准备上路了。')
    def stop(self):
        print(f'{self.name},Truck 准备停车。')
class BaoMa(Car):
    def driver(self):
        print(f'{self.name},BaoMa 要跑到100km了。')
    def stop(self):
        print(f'{self.name},BaoMa飘逸停车。')

class Person():
    def __init__(self,name):
        self.name=name
    def driverCar(self,car):
        print(f'{self.name},准备开-{car.name}-车上路了；')
        car.driver()
    def stopCar(self,car):
        print(f'{self.name},准备停-{car.name}-车。')
        car.stop()
'''
Car是一个抽象类，并不需要通过它创建实例对象，所以Car的实例方法都会抛出异常，由子类继承Car，然后重写方法才能正常使用；
'''
person=Person('ZBH')
truck=Truck('小卡车')
baoma=BaoMa('大宝马')
person.driverCar(truck)
person.stopCar(baoma)












