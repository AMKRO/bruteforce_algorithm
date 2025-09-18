characters = {
    "lowercase": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
    "uppercase": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
    "numbers": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "special": ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "/", "?"],
}
all_characters = characters["lowercase"] + characters["uppercase"] + characters["numbers"] + characters["special"]
# 92 in total
# 4 length in total
# 368 combinations 

def func_guessPass(str_pass):
    str_realPass = "abc"
    return str_pass == str_realPass

def func_cartesianProduct(iterable, repeat):
    pools = [tuple(iterable)] * repeat

    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]

    for prod in result:
        yield tuple(prod)

def func_bruteCrack(maximum_length):
    for int_length in range(1, maximum_length+1):
        for tuple_guess in func_cartesianProduct(all_characters, int_length):
            str_guessPassword = ''.join(tuple_guess)
            if func_guessPass(str_guessPassword):
                print("Found: ",str_guessPassword)
                return str_guessPassword
            else:
                print("Failed with: ",str_guessPassword)

func_bruteCrack(3)