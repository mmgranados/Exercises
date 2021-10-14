from random import uniform
from random import seed
seed()

class Team:

    def __init__(self, team_name:str, fantasy_pts_mean:float, stddev:float):
        self.name = team_name
        self.fantasy_pts_mean = fantasy_pts_mean
        self.stddev = stddev
        self.placements = {'13-16': 0, '9-12': 0, '7-8': 0, '5-6': 0, '4': 0, '3': 0, '2': 0, '1': 0}

    def get_name(self):
        return self.name

    def get_stddev(self):
        return self.stddev

    def get_fantasy_mean(self):
        return self.fantasy_pts_mean
    
    def set_stddev(self, stddev):
        self.stddev = stddev

    def set_fantasy_mean(self, mean):
        self.fantasy_pts_mean = mean
    
    def on_fire(self):
        """
        Team performance improves the more they advance
        Team perf goes up randomly from 1 to 2%
        
        """
        self.fantasy_pts_mean = self.fantasy_pts_mean * uniform(1.01, 1.02)

    def set_place(self, place):
        if place <= 16 and place >= 13:
            self.placements['13-16'] += 1
            return
        
        if place <= 12 and place >= 9:
            self.placements['9-12'] += 1
            return

        if place <= 8 and place >= 7:
            self.placements['7-8'] += 1
            return
        
        if place <= 6 and place >= 5:
            self.placements['5-6'] += 1
            return

        if place == 4:
            self.placements['4'] += 1
            return

        if place == 3:
            self.placements['3'] += 1
            return
        
        if place == 2:
            self.placements['2'] += 1
            return

        if place == 1:
            self.placements['1'] += 1
            return

    def print_placements(self):
        for placement, times in self.placements.items():
            print("{}: {} times".format(placement, times))



            


