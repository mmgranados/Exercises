from random import seed
from random import gauss
from random import uniform
from random import random
from Team import Team
seed()

class Tournament:

    def __init__(self, name:str, teams:Team):
        self.name = name
        self.UB = []
        self.LB = []
        self.UB_losers = []
        self.LB_winners = []
        self.placements = []
        self.teams = teams
    
    def on_fire(self,team):
        """"Team improves the more series they win(Either by mindset shifts or strat reveals"""
        team.on_fire()

    def generate_fantasy_pts(self, team): 
        """"Generate fantasy points(using gauss random) with luck as factor"""
        # generate gaussian random fantasy pts based on mean and stddev
        # multiply
        fantasy:float = gauss(team.get_fantasy_mean(), team.get_stddev())
        # print(fantasy)  
        luck:float = uniform((1/1.17), (1*1.17))
        # print(luck)
        return fantasy*luck  

    def simulate_match(self, team1:Team, team2:Team, best_of_n):
        """"Simulate a best of n match and return true if team 1 wins, returns false if team 2 wins"""
        best_of_n = best_of_n

        win_threshold = 0
        if (best_of_n == 5): win_threshold = 3
        if (best_of_n == 3): win_threshold = 2
        if (best_of_n == 1): win_threshold = 1

        team1_wins = 0
        team2_wins = 0

        while (team1_wins < win_threshold and team2_wins < win_threshold ):
            # current generated fantasy pts are 
            # returns true if team1 wins
            team1_fantasy_pts = self.generate_fantasy_pts(team1) * 5
            team2_fantasy_pts = self.generate_fantasy_pts(team2) * 5

            # 20-25 seems to be the threshold of almost certain winning so anything from 20 - 25 will be used
            prob_team1_wins = 1/ (1 + 10 ** ((team2_fantasy_pts - team1_fantasy_pts) / 22.5))
            
            if (random() < prob_team1_wins):
                # print("random is {}".format(random()))
                # print("prob_team1_wins is {}".format(prob_team1_wins))
                team1_wins += 1
            else: 
                # print("random is {}".format(random()))
                # print("prob_team1_wins is {}".format(prob_team1_wins))
                team2_wins += 1

        print("{} {}:{} {}".format(team1.get_name(), team1_wins, team2_wins, team2.get_name()))

        if (team1_wins > team2_wins):
            # teams that win become "on fire"/improve
            self.on_fire(team1)
            return True

        self.on_fire(team2)
        return False


    def init_brackets(self):
        for ub_team in self.teams[0:8]:
            self.UB.append(ub_team)
        for lb_team in self.teams[8:16]:
            self.LB.append(lb_team)


    def UB_round_1(self):

        best_of_n = 3
        x = 0
        while(x < len(self.UB)):
            print("{} vs {}".format(self.UB[x].get_name(), self.UB[x+1].get_name()))

            team1_wins = self.simulate_match(self.UB[x], self.UB[x+1], best_of_n)
            # print(team1_wins)
            if (team1_wins):
                print("{} advances!".format(self.UB[x].get_name()))
                self.UB_losers.append(self.UB[x+1])
            else:
                print("{} advances!".format(self.UB[x+1].get_name()))
                self.UB_losers.append(self.UB[x])  
            x += 2
        
        # remove the losers from the upper bracket
        for team in self.UB_losers:
            self.UB.remove(team)        

        # for team in self.UB: 
        #     print(team.get_name())
    
    def UB_round_2(self):
        """
        Remaining pairs of upper bracket teams fight
        losers go to LB round 4
        """
        # Refreshes list of upper bracket losers
        self.UB_losers.clear()
        best_of_n = 3
        x = 0
        while(x < len(self.UB)):
            print("{} vs {}".format(self.UB[x].get_name(), self.UB[x+1].get_name()))

            team1_wins = self.simulate_match(self.UB[x], self.UB[x+1], best_of_n)
            print(team1_wins)
            if (team1_wins):
                print("{} advances!".format(self.UB[x].get_name()))
                self.UB_losers.append(self.UB[x+1])
            else:
                print("{} advances!".format(self.UB[x+1].get_name()))
                self.UB_losers.append(self.UB[x])  
            x += 2

        for team in self.UB_losers:
            self.UB.remove(team)        

        # for team in self.UB: 
        #     print(team.get_name())

        return
        
    
    def UB_finals(self):
        """"Initiates match between the 2 remaining upper bracket teams"""
        best_of_n = 3
        # Refreshes list of upper bracket losers
        self.UB_losers.clear()
        x = 0
        while(x < len(self.UB)):
            print("{} vs {}".format(self.UB[x].get_name(), self.UB[x+1].get_name()))

            team1_wins = self.simulate_match(self.UB[x], self.UB[x+1], best_of_n)
            print(team1_wins)
            if (team1_wins):
                print("{} advances!".format(self.UB[x].get_name()))
                self.UB_losers.append(self.UB[x+1])
            else:
                print("{} advances!".format(self.UB[x+1].get_name()))
                self.UB_losers.append(self.UB[x])  
            x += 2

        for team in self.UB_losers:
            self.UB.remove(team)        

        # for team in self.UB: 
        #     print(team.get_name())

        return
    
    def grand_finals(self):

        self.UB_losers.clear()
        team1_wins = self.simulate_match(self.UB[0], self.LB[0], 5)
        winner = None

        # print(team1_wins)
        if (team1_wins):
            winner = self.UB[0]
            # print("{} is the winner of the Dota 2 International 2021!".format(self.UB[0].get_name()))
            self.UB_losers.append(self.LB[0])
        else:
            winner = self.LB[0]
            # print("{} is the winner of the Dota 2 International 2021!".format(self.LB[0].get_name()))
            self.UB_losers.append(self.UB[0])

        self.placements.append(self.UB_losers[0])
        self.placements.append(winner)

        
    def LB_round_1(self):
        """BO1 for LB teams"""
        # for team in self.LB:
        #     print(team.get_name())

        losers = []
        x = 0
        best_of_n = 1
        while(x < len(self.LB)):
            print("{} vs {}".format(self.LB[x].get_name(), self.LB[x+1].get_name()))

            team1_wins = self.simulate_match(self.LB[x], self.LB[x+1], 1)
            print(team1_wins)
            if (team1_wins):
                # print("{} advances!".format(self.LB[x].get_name()))
                losers.append(self.LB[x+1])
            else:
                # print("{} advances!".format(self.LB[x+1].get_name()))
                losers.append(self.LB[x])  
            x += 2

        # for team in self.LB: 
        #     print(team.get_name())

        # for team in losers: 
        #     print(team.get_name())    

        for team in losers: 
            self.placements.append(team)
            self.LB.remove(team)
            
        # print("LB round 1 winners: ")
        # for team in self.LB: 
            # print(team.get_name())

        return


    def LB_round_2(self):

        best_of_n = 3
        winners = []
        losers = []
        x = 0
        while(x < len(self.LB)):
            print("{} vs {}".format(self.LB[x].get_name(), self.UB_losers[x].get_name()))

            team1_wins = self.simulate_match(self.LB[x], self.UB_losers[x], best_of_n)
            # print(team1_wins)
            if (team1_wins):
                print("{} advances!".format(self.LB[x].get_name()))
                winners.append(self.LB[x])
                losers.append(self.UB_losers[x])
            else:
                print("{} advances!".format(self.UB_losers[x].get_name()))
                winners.append(self.UB_losers[x])  
                losers.append(self.LB[x])
            x += 1
        
        self.LB.clear()

        for team in losers:
            self.placements.append(team)
            # print(team.get_name())

        # print("Winners:")
        for team in winners: 
            self.LB.append(team)
            # print(team.get_name())


    def LB_round_3(self):

        losers = []
        x = 0
        best_of_n = 3

        while(x < len(self.LB)):
            print("{} vs {}".format(self.LB[x].get_name(), self.LB[x+1].get_name()))

            team1_wins = self.simulate_match(self.LB[x], self.LB[x+1], best_of_n)
            # print(team1_wins)
            if (team1_wins):
                print("{} advances!".format(self.LB[x].get_name()))
                losers.append(self.LB[x+1])
            else:
                print("{} advances!".format(self.LB[x+1].get_name()))
                losers.append(self.LB[x])  
            x += 2

        for team in losers: 
            self.placements.append(team)
            self.LB.remove(team)
            
        # print("LB round 3 winners: ")
        # for team in self.LB: 
        #     print(team.get_name())

        return


    def LB_round_4(self):

        best_of_n = 3
        winners = []
        losers = []
        x = 0
        while(x < len(self.LB)):
            print("{} vs {}".format(self.LB[x].get_name(), self.UB_losers[x].get_name()))

            team1_wins = self.simulate_match(self.LB[x], self.UB_losers[x], best_of_n)
            # print(team1_wins)
            if (team1_wins):
                print("{} advances!".format(self.LB[x].get_name()))
                winners.append(self.LB[x])
                losers.append(self.UB_losers[x])
            else:
                print("{} advances!".format(self.UB_losers[x].get_name()))
                winners.append(self.UB_losers[x])  
                losers.append(self.LB[x])
            x += 1
        
        # clears LB list and later append winners to it
        self.LB.clear()

        for team in losers:
            self.placements.append(team)
            # print(team.get_name())

        # print("Winners:")
        for team in winners: 
            self.LB.append(team)
            # print(team.get_name())

    
        return

    def LB_round_5(self):

        losers = []
        x = 0
        best_of_n = 3

        while(x < len(self.LB)):
            print("{} vs {}".format(self.LB[x].get_name(), self.LB[x+1].get_name()))

            team1_wins = self.simulate_match(self.LB[x], self.LB[x+1], best_of_n)
            # print(team1_wins)
            if (team1_wins):
                print("{} advances!".format(self.LB[x].get_name()))
                losers.append(self.LB[x+1])
            else:
                print("{} advances!".format(self.LB[x+1].get_name()))
                losers.append(self.LB[x])  
            x += 2

        for team in losers: 
            self.placements.append(team)
            self.LB.remove(team)
            
        # print("LB round 5 winners: ")
        # for team in self.LB: 
        #     print(team.get_name())

        return

    def LB_finals(self):
        "Simulates a match between the 2 remaining teams in the lower bracket"
        
        best_of_n = 3    
        winners = []
        losers = []
        x = 0
    
        while(x < len(self.LB)):
            print("{} vs {}".format(self.LB[x].get_name(), self.UB_losers[x].get_name()))

            team1_wins = self.simulate_match(self.LB[x], self.UB_losers[x], best_of_n)
            # print(team1_wins)
            if (team1_wins):
                print("{} advances!".format(self.LB[x].get_name()))
                winners.append(self.LB[x])
                losers.append(self.UB_losers[x])
            else:
                print("{} advances!".format(self.UB_losers[x].get_name()))
                winners.append(self.UB_losers[x])  
                losers.append(self.LB[x])
            x += 1
        
        # clears LB list and later append winners to it
        self.LB.clear()

        for team in losers:
            self.placements.append(team)
            # print(team.get_name())

        print("Winners:")
        for team in winners: 
            self.LB.append(team)
            # print(team.get_name())

        return


    def record_placements(self):
        x = 16
        for team in self.placements:
            # print("{} - place: {}".format(team.get_name(), x))
            team.set_place(x)
            x -= 1


    def simulate_tournament(self):
        
        self.UB_round_1()

        self.LB_round_1()

        self.LB_round_2()

        # print("")
        # print("After LB round 2:")
        # print("Upper bracket teams:")
        # for team in self.UB:
        #     print(team.get_name())

        # print("Lower bracket teams:")
        # for team in self.LB:
        #     print(team.get_name())

        
        self.LB_round_3()

        # print("")
        # print("After LB round 3:")
        # print("Upper bracket teams:")
        # for team in self.UB:
        #     print(team.get_name())
        # print("Lower bracket teams:")
        # for team in self.LB:
        #     print(team.get_name())

        self.UB_round_2()
        # print("")
        # print("After UB Round 2:")
        # print("Upper bracket teams:")
        # for team in self.UB:
        #     print(team.get_name())
        
        self.LB_round_4()
        # print("")
        # print("After LB round 4:")
        # print("Lower bracket teams:")
        # for team in self.LB:
        #     print(team.get_name())

        self.LB_round_5()
        self.UB_finals()

        # print("")
        # print("After UB Finals:")
        # print("Upper bracket teams:")
        # for team in self.UB:
        #     print(team.get_name())
        # print("Lower bracket teams:")
        # for team in self.LB:
        #     print(team.get_name())

        self.LB_finals()
        self.grand_finals()

        self.record_placements()

        



        



        
        
        
    
    
            
        
    
    


    
    



    





    
    


