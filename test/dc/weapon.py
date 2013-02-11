class Weapon:
    """Instantiates a weapon()"""
    def __init__(self,damage=[2,1],element="None",statboost=[0,0,0,0]):
        self.damage=damage
        self.element=element
        self.statboost=statboost
    
#damage[min,addUpTo], element, statboost[str,def,agi,int
fists=Weapon()
sword=Weapon()