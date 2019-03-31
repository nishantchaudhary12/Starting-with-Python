#world series champions


def teams_record():
    file = open("WorldSeriesWinners.txt", "r")
    teams = list()
    while True:
        name = file.readline()
        if name == '':
            break
        name = name.rstrip('\n')
        teams.append(name)
    file.close()
    return teams


def main():
    teams = teams_record()
    team_name = input("Enter the name of the team: ")
    print(team_name, 'won the world series', teams.count(team_name), 'times.')


main()