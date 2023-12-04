def get_sets(l: list):
    """
    Separates an array of games into a dict of games with their associated sets as a list of lists

    Args:
        l (list): An array of game info

    Returns:
        games (dict): Key is game ID, val is a list of game sets
    """
    games = {}
    x = 0
    for game in l:
        x += 1
        start = game.index(':')
        games[str(x)] = game[start+2:].split(';')
    
    return games   


def possible_games(infile):
    """
    Determines if a game is possible given the number of blocks available and sums the ID's of the valid games

    Args: 
        infile (file): file containing game results
    Returns:
        games_sum (int): the sume of the valid game ID's
    """
    blocks_held = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    games_sum = 0
    lines = []

    with open(infile, 'r') as f:
        for line in f:
            lines.append(line.strip('\n'))
    
    games = get_sets(lines)

    for key in games:
        is_possible = True

        for set in games[key]:
            if not is_possible:
                break
            colors = set.split(',')
            
            for color in colors:
                if not is_possible:
                    break
                tmp = color.split()
                if 'blue' in tmp:
                    is_possible = int(tmp[0]) <= blocks_held['blue']
                elif 'red' in tmp:
                    is_possible = int(tmp[0]) <= blocks_held['red']
                else:
                    is_possible = int(tmp[0]) <= blocks_held['green']
        
        if is_possible:
            games_sum += int(key)
    
    print(games_sum)
    return games_sum
            

    

if __name__ == "__main__":
    possible_games('input.txt')