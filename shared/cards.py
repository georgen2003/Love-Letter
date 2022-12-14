class Card(object):
    def __init__(self):
        self.id = -1
        self.power = -1
        self.name = "Invalid"
        self.description = "Invalid"
        
    def played(self, player, client):
        pass
    
    def discarded(self, player, client, prey):
        pass
    
    def answer(self, hunter_id, prey_id, prey_card, players_info, eliminated, used):
        pass
    
class Assassin(Card):
    def __init__(self):
        super().__init__()
        self.id = 0
        self.power = 0
        self.name = "Assassin"
        self.description = "If a player targets you with a Guard, you eliminate them and discard this card."
    
    def played(self, player, client):
        pass

    def discarded(self, player, client, prey):
        pass

    def answer(self, hunter_id, prey_id, prey_card, players_info, eliminated, used):
        pass
    
class Guard(Card):
    def __init__(self):
        super().__init__()
        self.id = 1
        self.power = 1
        self.name = "Guard"
        self.description = "Guess a player's non guard card. If you are correct, that player is eliminated."
        
    def played(self, player, client):

        if player.selected_target == -1:
            player.choose_player([], self.id)
            return
        
        if player.target_card == -1:
            player.target_card = player.choose_card(self.id)
            return

        self.discarded(player, client, player.selected_target, player.target_card)

    
    def discarded(self, player, client, prey, prey_card):
        client.play_move(self.id, prey, prey_card)
        return
    
    def answer(self, hunter_id, prey_id, prey_card, players_info, eliminated, used):
        if prey_card == -1:
            return -1

        if 0 in players_info[prey_id]["hand"]:
            used.append(players_info[prey_id]["hand"].remove(0))

            while len(players_info[hunter_id]["hand"]) != 0:
                used.append(players_info[hunter_id]["hand"].pop())

            eliminated.append(hunter_id)
            players_info[hunter_id]["eliminated"] = True
            return hunter_id

        if prey_card in players_info[prey_id]["hand"] :
            used.append(players_info[prey_id]["hand"].remove(prey_card))
            eliminated.append(prey_id)
            players_info[prey_id]["eliminated"] = True
            return prey_id

        return 0
        
    
class Priest(Card):
    def __init__(self):
        super().__init__()
        self.id = 2
        self.power = 2
        self.name = "Priest"
        self.description = "Look at another player's card."
        
    def played(self, player, client):
        target = player.choose_player([], self.id)
        return "!PRIEST$" + str(target) + "$" + str(player.player_id)
    
    def discarded(self, player, client, prey):
        pass
    
    def answer(self, hunter_id, prey_id, prey_card, players_info, eliminated, used):
        pass
    
class Baron(Card):
    def __init__(self):
        super().__init__()
        self.id = 3
        self.power = 3
        self.name = "Baron"
        self.description = "Compare hands with another player. The player with the least power is eliminated."
        
    def played(self, player, client):
        target = player.choose_player([], self.id)
        # return "!BARON$" + str(target) + "$" + str(player.player_id)
    
    def discarded(self, player, client, prey):
        pass
    
    def answer(self, hunter_id, prey_id, prey_card, players_info, eliminated, used):
        pass


card_dict = {
            #0: {"card": Assassin, "count": 1, "image": "./images/guard.jpg"},
            1: {"card": Guard(), "count": 5, "image": "./images/guard.jpg"},
            #2: {"card": Priest, "count": 2, "image": "./images/baron.jpg"},
            3: {"card": Baron(), "count": 2, "image": "./images/baron.jpg"},
        }

