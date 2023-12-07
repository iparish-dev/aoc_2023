def count_cards(infile):
    winning_nums = ''
    total_score = 0
    lines = []
    games = {}

    with open(infile) as f:
        for line in f:
         lines.append(line)
    
    x = 1
    for line in lines:
        start = line.index(':')
        end = line.index('|')
        games[x] = line[start + 1:end].split()
        x += 1

        winning_nums += line[end+2:].strip('\n')
    
    winning_nums = winning_nums.split()
    
    for key in games:
        num_matches = 0
        for num in games[key]:
            if num in winning_nums:
                #TODO
        card_score = num_matches^2
        total_score += card_score
        


if __name__ == "__main__":
    count_cards('input.txt')