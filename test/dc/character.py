class Character:
    """Instantiates a Character(name,level[cur_lvl,cur_xp,xp_tnl],HP[cur,max,growth],SP[name,cur,max,growth],equip=[6*4 array of stat boosts for HP,SP,str,def,int,agi],str,def,int,agi,status,extradata[])"""

    def __init__(self,name='Player',level=[1,0,8],HP=[10,10,1],SP=['Special',10,10,1],equip=[[0]*6]*4,strength=5,defense=5,intelligence=5,agility=5,status="None",data=[]):
        print 'Character instantiated'
        self.name=name
        self.level=level
        self.HP=HP
        self.SP=SP
        self.strength=strength
        self.defense=defense
        self.intelligence=intelligence
        self.agility=agility
        self.status=status
        self.equip=equip
        self.data=data

blankplayer=Character()