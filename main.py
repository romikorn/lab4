class Ship:
    '''
    корабль имеет длину, ширину, водоизмещение, скорость, очки здоровья
    и урон в секунду. может атаковать и получать урон, а также плыть
    при получении урона ухудшается скорость и урон в секунду
    '''
    def __init__(self, width, length, displacement, speed, full_hp, damage_per_second):
        self.width = width
        self.length = length
        self.displacement = displacement
        self.speed = speed
        self.full_hp = full_hp
        self.damage_per_second = damage_per_second
        self.hp = self.full_hp

    def attack(self, time):
        return self.damage_per_second * time

    def receive_damage(self, received_damage):
        self.hp = self.hp - received_damage
        self.speed = self.speed*0.3*self.hp/self.full_hp + 0.7*self.speed
        self.damage_per_second = self.damage_per_second*0.2*self.hp/self.full_hp + 0.8*self.damage_per_second
        if self.hp <= 0:
            self.hp = "уничтожен"
        return self.hp

    def sailing_distance(self, time):
        return self.speed*time

    def print_info(self):
        print(f"Ширина:{self.width} Длина:{self.length} Водоизмещение:{self.displacement} Скорость: {self.speed}  Здоровье: {self.hp} Урон в секунду: {self.damage_per_second}")


class Plane:
    '''
    самолет имеет длину, размах крыльев, вес, скорость, очки здоровья
    и урон в секунду. может атаковать и получать урон, а также летать
    при получении урона ухудшается скорость и урон в секунду
    '''
    def __init__(self, wingspan, length, weight, speed, full_hp, damage_per_second):
        self.wingspan = wingspan
        self.length = length
        self.weight = weight
        self.speed = speed
        self.full_hp = full_hp
        self.damage_per_second = damage_per_second
        self.hp = self.full_hp

    def attack(self, time):
        return self.damage_per_second * time

    def receive_damage(self, received_damage):
        self.hp = self.hp - received_damage
        self.speed = self.speed * 0.3 * self.hp / self.full_hp + 0.7 * self.speed
        self.damage_per_second = self.damage_per_second * 0.2 * self.hp / self.full_hp + 0.8 * self.damage_per_second
        if self.hp <= 0:
            self.hp = "уничтожен"
        return self.hp

    def flying_distance(self, time):
        return self.speed*time

    def print_info(self):
        print(f"Размах крыльев:{self.wingspan} Длина:{self.length} Вec:{self.weight} Скорость: {self.speed} Здоровье: {self.hp} Урон в секунду: {self.damage_per_second}")


class Destroyer(Ship):
    def __init__(self):
        super().__init__(7.5,20,3000, 60.0, 2500.0, 100)

    def print_info(self):
        print("Информация про  корабль Destroyer:")
        super().print_info()


class Cruiser(Ship):
    '''
    имеет 4 торпеды, которыми миожет наносить урон
    '''
    def __init__(self):
        super().__init__(10, 30, 6000, 50.0, 5000.0, 150)
        self.torpedos = 4

    def launch_torpedo(self, count):
        self.torpedo_damage = 0
        if count <= self.torpedos and self.torpedos > 0:
            self.torpedo_damage += 250*count
            self.torpedos = self.torpedos - count
            return self.torpedo_damage
        elif count > self.torpedos and self.torpedos != 0:
            self.torpedo_damage += 250*self.torpedos
            self.torpedos = 0
            return self.torpedo_damage
        else:
            print("Торпеды кончились")
            return self.torpedo_damage

    def print_info(self):
        print("Информация про  корабль Cruiser:")
        super().print_info()


class HeavyCruiser(Ship):
    '''
    имеет 6 торпед и 2 больших торпед, которыми миожет наносить урон
    '''
    def __init__(self):
        super().__init__(12.5, 40, 10000, 40.0, 7500.0, 250)
        self.torpedos = 6
        self.bigtorpedos = 2

    def launch_torpedo(self, count):
        self.torpedo_damage = 0
        if count <= self.torpedos and self.torpedos > 0:
            self.torpedo_damage += 250*count
            self.torpedos = self.torpedos - count
            return self.torpedo_damage
        elif count > self.torpedos and self.torpedos != 0:
            self.torpedo_damage += 250*self.torpedos
            self.torpedos = 0
            return self.torpedo_damage
        else:
            print("Торпеды кончились")
            return self.torpedo_damage

    def launch_bigtorpedo(self, count):
        self.torpedo_damage = 0
        if count <= self.bigtorpedos and self.bigtorpedos > 0:
            self.torpedo_damage += 500*count
            self.bigtorpedos = self.bigtorpedos - count
            return self.torpedo_damage
        elif count > self.bigtorpedos and self.bigtorpedos != 0:
            self.torpedo_damage += 500*self.bigtorpedos
            self.bigtorpedos = 0
            return self.torpedo_damage
        else:
            print("Большие торпеды кончились")
            return self.torpedo_damage

    def print_info(self):
        print("Информация про  корабль HeavyCruiser:")
        super().print_info()


class BattleShip(Ship):
    '''
    имеет 10 торпед, 4 больших торпед и 3 ракеты, которыми миожет наносить урон
    '''
    def __init__(self):
        super().__init__(17, 55, 20000, 35.0, 12500.0, 500)
        self.torpedos = 10
        self.bigtorpedos = 4
        self.rockets = 3

    def launch_torpedo(self, count):
        self.torpedo_damage = 0
        if count <= self.torpedos and self.torpedos > 0:
            self.torpedo_damage += 250 * count
            self.torpedos = self.torpedos - count
            return self.torpedo_damage
        elif count > self.torpedos and self.torpedos != 0:
            self.torpedo_damage += 250 * self.torpedos
            self.torpedos = 0
            return self.torpedo_damage
        else:
            print("Торпеды кончились")
            return self.torpedo_damage

    def launch_bigtorpedo(self, count):
        self.torpedo_damage = 0
        if count <= self.bigtorpedos and self.bigtorpedos > 0:
            self.torpedo_damage += 500 * count
            self.bigtorpedos = self.bigtorpedos - count
            return self.torpedo_damage
        elif count > self.bigtorpedos and self.bigtorpedos != 0:
            self.torpedo_damage += 500 * self.bigtorpedos
            self.bigtorpedos = 0
            return self.torpedo_damage
        else:
            print("Большие торпеды кончились")
            return self.torpedo_damage

    def launch_rocket(self, count):
        self.rocket_damage = 0
        if count <= self.rockets and self.rockets > 0:
            self.rocket_damage += 650 * count
            self.rockets = self.rockets - count
            return self.rocket_damage
        elif count > self.rockets and self.rockets != 0:
            self.rocket_damage += 650 * self.rockets
            self.rockets = 0
            return self.rocket_damage
        else:
            print("Ракеты кончились")
            return self.rocket_damage

    def print_info(self):
        print("Информация про  корабль BattleShip:")
        super().print_info()

class Fighter(Plane):
    def __init__(self):
        super().__init__(9, 7, 3, 400.0, 150.0, 25)

    def print_info(self):
        print("Информация про самолет Fighter:")
        super().print_info()

class LightBomber(Plane):
    '''
    имеет 2 бомбы, которыми миожет наносить урон
    '''
    def __init__(self):
        super().__init__(12, 8, 4, 325.0, 250.0, 25)
        self.bombs = 2

    def drop_bomb(self, count):
        self.bomb_damage = 0
        if count <= self.bombs and self.bombs > 0:
            self.bomb_damage += 350 * count
            self.bombs = self.bombs - count
            return self.bomb_damage
        elif count > self.bombs and self.bombs != 0:
            self.bomb_damage += 350 * self.bombs
            self.bombs = 0
            return self.bomb_damage
        else:
            print("Бомбы кончились")
            return self.bomb_damage

    def print_info(self):
        print("Информация про самолет LightBomber:")
        super().print_info()

class HeavyBomber(Plane):
    '''
    имеет 5 бомб и 1 торпеду, которыми миожет наносить урон
    '''
    def __init__(self):
        super().__init__(15, 10, 7, 275.0, 400.0, 30)
        self.bombs = 5
        self.torpedos = 1

    def drop_bomb(self, count):
        self.bomb_damage = 0
        if count <= self.bombs and self.bombs > 0:
            self.bomb_damage += 350 * count
            self.bombs = self.bombs - count
            return self.bomb_damage
        elif count > self.bombs and self.bombs != 0:
            self.bomb_damage += 350 * self.bombs
            self.bombs = 0
            return self.bomb_damage
        else:
            print("Бомбы кончились")
            return self.bomb_damage

    def drop_torpedo(self, count):
        self.torpedo_damage = 0
        if count <= self.torpedos and self.torpedos > 0:
            self.torpedo_damage += 400 * count
            self.torpedos = self.torpedos - count
            return self.torpedo_damage
        elif count > self.torpedos and self.torpedos != 0:
            self.torpedo_damage += 400 * self.torpedos
            self.torpedos = 0
            return self.torpedo_damage
        else:
            print("Торпеды кончились")
            return self.torpedo_damage

    def print_info(self):
        print("Информация про самолет HeavyBomber:")
        super().print_info()


obj_destroyer = Destroyer()
obj_fighter = Fighter()
obj_cruiser = Cruiser()
obj_heavybomber = HeavyBomber()
obj_battleship = BattleShip()

print("Самолет Fighter наносит кораблю Destroyer урон в течении 5 секунд")
obj_destroyer.receive_damage(obj_fighter.attack(5))
obj_destroyer.print_info()
print("Корабль Destroyer наносит  урон самолету Fighter в течении 1 секунды")
obj_fighter.receive_damage(obj_destroyer.attack(1))
obj_fighter.print_info()
print("Самолет HeavyBomber кидает в корабль Cruiser 5 бомб")
obj_cruiser.receive_damage(obj_heavybomber.drop_bomb(5))
obj_cruiser.print_info()
print("Корабль Destroyer наносит  урон самолету HeavyBomber в течении 2 секунд")
obj_heavybomber.receive_damage(obj_destroyer.attack(2))
obj_heavybomber.print_info()
print("Корабль Cruiser запускает в корабль Destroyer 4 торпеды")
obj_destroyer.receive_damage(obj_cruiser.launch_torpedo(4))
obj_destroyer.print_info()
print("Корабль BattleShip наносит урон кораблю Cruiser в течение 5 секунд и запускает в него 2 ракеты")
obj_cruiser.receive_damage(obj_battleship.attack(5))
obj_cruiser.receive_damage(obj_battleship.launch_rocket(2))
obj_cruiser.print_info()
print("Самолет Fighter наносит урон самолету HeavyBomber в течение 10 секунд")
obj_heavybomber.receive_damage(obj_fighter.attack(10))
obj_heavybomber.print_info()




'''destroyer1 = Destroyer()
destroyer1.print_info()
print(f"{destroyer1.attack(3)}")

cruiser1 = Cruiser()
#cruiser1.launch_torpedo(2)
cruiser1.print_info()

destroyer1.current_hp(cruiser1.launch_torpedo(4))
print(f"{destroyer1.hp}")

lightbomber1 = LightBomber()
lightbomber1.print_info()



#print(f"{cruiser1.attack_damage(4)}")
#cruiser1.print_info(Cruiser)
#Cruiser = Ship(10, 30, 7.5, 100)
#print(f"{Ship.width}")'''