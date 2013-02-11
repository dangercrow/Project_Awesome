import character
import weapon

class Battle:
    """Instantiates a Battle([character,weapon]*8) consisting of up to 4 PCs and 4 NPCs"""
    def __init__(self, player1=[character.blankplayer,weapon.sword],player2=None,player3=None,player4=None,
                    enemy1=[blankenemy,weapon.fists],enemy2=None,enemy3=None,enemy4=None):
        #Consider tuples for players? Consider effect of None in player types
        
battle = Battle()