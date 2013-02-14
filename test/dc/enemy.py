class Enemy:
    """Instantiates an Enemy(name,level,HP[cur,max],SP[name,cur,max],str,def,int,agi,status,extradata[])"""
    def __init__(self,name='Enemy',level=1,HP=[10,10],SP=['Special',10,10],
                      strength=1,defense=1,intelligence=1,agility=1,status='None',ai='Random',xp=1,data=[]):
        print 'Enemy instantiated'
        self.name=name
        self.level=level
        self.HP=HP
        self.SP=SP
        self.strength=strength
        self.defense=defense
        self.intelligence=intelligence
        self.agility=agility
        self.status=status
        self.ai=ai
        self.xp=xp
        self.data=data

blankenemy=Enemy()