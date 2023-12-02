def get_calibration_value(infile):
    words = []
    numvals = []
    with open(infile, 'r') as f:
        for line in f:
            words.append(line.strip())
    
    for word in words:
        num1 = None
        num2 = None
        for letter in word:
            if letter.isnumeric() and num1 == None:
                num1 = letter
            elif letter.isnumeric():
                num2 = letter
        if num2 == None:
            num2 = num1
        
        numvals.append(int(str(num1) + str(num2))) 
    
    return sum(numvals)
    
                



if __name__ == "__main__":
    get_calibration_value('input.txt')
