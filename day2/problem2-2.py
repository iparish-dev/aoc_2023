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


def set_power_sum(infile):
    """
    Determines the fewest amount of cubes required to make a game possible. 
    Multiplies the number of each color cube for each game, and sums all of the games.
    
    Args:
        infile (file): file of game information

    Returns:
        power_sum (int): the sum of the 'power' of each game
    """
    power_sum = 0
    lines = []

    with open(infile, 'r') as f:
        for line in f:
            lines.append(line.strip('\n'))
    
    games = get_sets(lines)

    for key in games:
        red_max =   0
        blue_max =  0
        green_max = 0

        for set in games[key]:
            colors = set.split(',')
            
            for color in colors:
                tmp = color.split()
                if 'blue' in tmp:
                    blue_max = int(tmp[0]) if int(tmp[0]) > blue_max else blue_max
                elif 'red' in tmp:
                    red_max = int(tmp[0]) if int(tmp[0]) > red_max else red_max
                else:
                    green_max = int(tmp[0]) if int(tmp[0]) > green_max else green_max
        
        power_sum += red_max * blue_max * green_max

    print(power_sum)
    return power_sum


if __name__ == "__main__":
    set_power_sum('input.txt')