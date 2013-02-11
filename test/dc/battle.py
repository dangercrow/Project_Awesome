import character
import enemy
import weapon

class Battle:
    """Instantiates a Battle([character,weapon]*4, [enemy,weapon]*4) consisting of up to 4 PCs and 4 NPCs"""
    def __init__(self, player1=[character.blankplayer,weapon.sword],player2=None,player3=None,player4=None,
                    enemy1=[enemy.blankenemy,weapon.fists],enemy2=None,enemy3=None,enemy4=None):
        #Consider tuples for players? Consider effect of None in player types
        print 'Battle instantiated'
        self.inprogress=False

currentbattle = Battle()

def clock():
    i=1
    print 'clock'
    i+=1
    if i>5:
        currentbattle.inprogress=True
    
def startBattle():
    while currentbattle.inprogress:
        clock()