from Tournament import Tournament
from Team import Team
from functools import lru_cache
from tqdm import tqdm


def reset_baseline_performance(teams):
    teams[0].set_fantasy_mean(1195.9 / (16*5))
    teams[1].set_fantasy_mean(1084.6 / (16*5))

    teams[2].set_fantasy_mean(1145.8 / (16*5))
    teams[3].set_fantasy_mean(1111 / (16*5))

    teams[4].set_fantasy_mean(1162.6 / (16*5))
    teams[5].set_fantasy_mean(1159.9 / (16*5))

    teams[6].set_fantasy_mean(1168.4 / (16*5))
    teams[7].set_fantasy_mean(1076.2 / (16*5))
    
    teams[8].set_fantasy_mean(1130.7 / (16*5))
    teams[9].set_fantasy_mean(1176.2 / (16*5))
    
    teams[10].set_fantasy_mean(1054.2 / (16*5))
    teams[11].set_fantasy_mean(970.4 / (16*5))

    teams[12].set_fantasy_mean(1085.2 / (16*5))
    teams[13].set_fantasy_mean(961.9 / (16*5))

    teams[14].set_fantasy_mean(1069.8 / (16*5))
    teams[15].set_fantasy_mean(1073.9 / (16*5))


def init_teams():

    teams = []
    IG = Team("IG", (1195.9 / (16*5)),  4.4338)
    TeamSpirit = Team("TeamSpirit", (1084.6 / (16*5)),  4.1866)

    TeamSecret = Team("TeamSecret", (1145.8 / (16*5)),  5.419)
    OG = Team("OG", (1111 / (16*5)),  4.7339)

    PSGLGD = Team("PSG.LGD", (1162.6 / (16*5)),  3.783)
    T1 = Team("T1", (1159.9 / (16*5)),  5.9009)

    VG = Team("VG", (1168.4 / (16*5)),  4.8209)
    VP = Team("VP", (1076.2 / (16*5)),  4.2638)
    
    Undying = Team("Undying", (1130.7 / (16*5)),  5.1094)
    Fnatic = Team("Fnatic", (1176.2 / (16*5)),  4.8057)
    
    QuincyCrew = Team("QuincyCrew", (1054.2 / (16*5)),  4.2951)
    TeamAster = Team("TeamAster", (970.4 / (16*5)),  4.41)

    Beastcoast = Team("Beastcoast", (1085.2 / (16*5)),  4.564)
    Alliance = Team("Alliance", (961.9 / (16*5)),  4.0996)

    EG = Team("EG", (1069.8 / (16*5)),  4.4069)
    Elephant = Team("Elephant", (1073.9 / (16*5)),  4.4482)

    teams.append(IG)
    teams.append(TeamSpirit)
    teams.append(TeamSecret)
    teams.append(OG)
    teams.append(PSGLGD)
    teams.append(T1)
    teams.append(VG)
    teams.append(VP)
    teams.append(Undying)
    teams.append(Fnatic)
    teams.append(QuincyCrew)
    teams.append(TeamAster)
    teams.append(Beastcoast)
    teams.append(Alliance)
    teams.append(EG)
    teams.append(Elephant)

    return teams


def main():
    
    teams = init_teams()

    
    simulations = 0
    for simulations in tqdm(range(10000)):
        reset_baseline_performance(teams)

        TI = Tournament("Dota 2 The International 2021", teams)

        # Check fantasy pts generator
        # loops = 0
        # Secret_wins = 0
        # OG_wins = 0
        # while(loops < 1000):
        #     # Returns true if team 1 wins
        #     if (TI.simulate_match(TeamSecret, OG, 3)):
        #         Secret_wins += 1
        #     else: 
        #         OG_wins += 1

        #     loops += 1

        # print("Team Secret wins {} times out of 1000".format(Secret_wins))
        # print("OG wins {} times out of 1000".format(OG_wins))

        # return -1
        TI.init_brackets()
        TI.simulate_tournament()

        
        
        simulations += 1
    
    print("Placement results")
    print("for 10000 games:")
    for team in teams:
        print("")
        print(team.get_name())
        team.print_placements()

main()
        
    

    

