class Weapon:
    """Instantiates a weapon(damage[min,addUpTo], element, statboost[str,def,agi,int])"""
    def __init__(self,damage=[1,1],element="None",statboost=[0,0,0,0]):
        self.damage=damage
        self.element=element
        self.statboost=statboost

    def info(self):
        print 'Damage:', weapon.damage[0],'-',weapon.damage[1]
        print 'Element:', weapon.element
        print 'Stat Boosts:','Strength:',weapon.statboost[0],'Defense:',weapon.statboost[0],'Intelligence:',weapon.statboost[0],'Agility:',weapon.statboost[0]

fists=Weapon()
sword=Weapon([2,1])