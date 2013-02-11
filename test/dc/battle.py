import character
import enemy
import weapon
import random

class Battle:
    """Instantiates a Battle([character,weapon]*4, [enemy,weapon]*4) consisting of up to 4 PCs and 4 NPCs"""
    def __init__(self, player1=[character.blankplayer,weapon.sword],player2=None,player3=None,player4=None,
                    enemy1=[enemy.blankenemy,weapon.fists],enemy2=None,enemy3=None,enemy4=None):
        #Consider tuples for players? Consider effect of None in player types
        print 'Battle instantiated'
        self.player1=player1
        self.player2=player2
        self.player3=player3
        self.player4=player4
        self.enemy1=enemy1
        self.enemy=enemy2
        self.enemy3=enemy3
        self.enemy3=enemy4
        self.result=0

currentbattle = Battle()
print

clockcount=1
def clock(battle):
    global clockcount
    print 'clock',clockcount
    clockcount+=1
    if clockcount>10:
        battle.result=int(random.random()+1.5) #Break out after 10 rounds for convenience
        return battle.result
    if battle.player1[0].HP[0]<1:
        battle.result=2 # Failure
        return battle.result
    elif battle.enemy1[0].HP[0]<1:
        battle.result=1 # Success
        return battle.result
    return 0 #In progress

def startBattle(battle):
    status=0
    while status==0:
        status=clock(battle)
    return status

result=startBattle(currentbattle)
        
if(result==1):
    print 'Victory!'
elif(result==2):
    print 'Failure.'