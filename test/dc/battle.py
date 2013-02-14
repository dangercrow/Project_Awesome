import character
import enemy
import weapon
import random

clockcount=1
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
        self.players=[player1,player2,player3,player4]
        self.playercount=0
        self.enemycount=0
        self.enemy1=enemy1
        self.enemy2=enemy2
        self.enemy3=enemy3
        self.enemy4=enemy4
        self.enemies=[enemy1,enemy2,enemy3,enemy4]
        self.result=0
        for i in range(0,4):
            if type(self.players[i])==type([]):
                self.playercount+=1
        for i in range(0,4):
            if type(self.enemies[i])==type([]):
                self.enemycount+=1
        self.max_agi=0 # Filled in startBattle()
        self.agi_check=[[0.0]*(self.playercount),[0.0]*(self.enemycount)]

    def clock(self):
        global clockcount
        print 'Clock',clockcount
        clockcount+=1
        if clockcount>10:
            self.result=int(random.randint(1,2)) #Break out after 10 rounds for convenience
            return self.result
        if self.player1[0].HP[0]<1:
            self.result=2 # Failure
            return self.result
        elif self.enemy1[0].HP[0]<1:
            self.result=1 # Success
            return self.result
        elif max(self.agi_check[0])>float(self.max_agi):
            return 3 #Player input time!
        return 0 #In progress
        

    def item(self,player,item):
        print player,'used item:',item

    def run(self,player):
        agi=player.agility
        return (random.randint(0,100)<agi+5)
    
    def rest(self,player):
        player.HP[0]+=3
        if player.HP[0]>player.HP[1]:player.HP[0]=player.HP[1]
        player.SP[0]+=3
        if player.SP[0]>player.SP[1]:player.SP[0]=player.SP[1]

    def damage(self,target,amount):
        target.HP[0]-=amount
        if target.HP[0]<0:target.HP[0]=0
        if target.HP[0]>target.HP[1]:target.HP[0]=target.HP[1]
        
    def attack(self,attacker,target):
        """player1 attacks enemy2, call attack(battle.player1,battle.enemy2)"""
        
        amount=random.randint(attacker[1].damage[0],attacker[1].damage[1])
        self.damage(target[0],amount)

    def startBattle(self):
        global clockcount
        clockcount=1
        status=0
        l_agi=[]
        for i in range(0,self.playercount):
            l_agi.append(self.players[i][0].agility)
        self.max_agi=max(l_agi)
        while (status==0)|(status==3):
            status=self.clock()
        return status

    def enemyAttack(self,enemy):
        if enemy[0].ai=='Random':
            t=random.randint(0,self.playercount-1)
            target=self.players[t]
            print t
            self.attack(enemy,target)

currentbattle = Battle()
result=currentbattle.startBattle()
print
        
if(result==1):
    print 'Victory!'
elif(result==2):
    print 'Failure.'

def test(count=1000):
    l=[0,0]
    for i in range(0,count):
        if currentbattle.run(currentbattle.player1[0]):
            l[0]+=1
        else:
            l[1]+=1
    print l