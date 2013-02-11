class Character:
    """Instantiates a Character(name,level[cur_lvl,cur_xp,xp_tnl],HP[cur,max,growth],SP[name,cur,max,growth],str,def,int,agi,status,extradata[])"""
    def __init__(self,name='Player',level=[1,0,8],HP=[10,10,1],SP=['Special',10,10,1],
                      strength=5,defense=5,intelligence=5,agility=5,status="None",data=[]):
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
        self.data=data

def info(character):
    print character.name, 'info:'
    print 'Level:', character.level[0]
    print 'XP:', character.level[1],'/',character.level[2]
    print 'HP:', character.HP[0],'/',character.HP[1]
    print character.SP[0],':', character.SP[1],'/',character.SP[2]
    print 'Strength:',character.strength
    print 'Defense:',character.defense
    print 'Intelligence:',character.intelligence
    print 'Agility:',character.agility
    print 'Status:',character.status
    print 'Extra Data:',character.data

blankplayer=Character()
hitler=Character('Adolf Hitler',[99,162,1239],[413,1337,0],['Gas chambers:',3,10,1],15,10,13,20,"None",['Has a tendency to kill everyone with Nazi powers','Only has one testicle'])

