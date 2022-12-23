# roman numbers are written from left to right from largest to smallest.eg 1012 will be written as
# MXII
# There are special cases when we put teh smaller one fast.
# here we are basically subtracting the value of the smaller one from the value of the bigger
# for instance we write 4 as IV (in essence what we are doing is we are subtracting one from five to get four)
# there are three such cases:
# I can be placed before V (5)  and X (10) to make 4 and 9, here 1 acts as -1
# X can be place before L(50) and M(1000) to make 40 and 90
# C can be placed before D(500) and M(1000) to make 400 and 900

# This program should output a correct integer given a string of roman numerals
def roman_to_int(roman):
    roman_no = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    for s in range(len(roman)):
        if s + 1 < len(roman) and roman_no[roman[s]] < roman_no[roman[s + 1]]:
            result -= roman_no[roman[s]]
        else:
            result += roman_no[roman[s]]
    return print(result)


s = 'LXVIII'
roman_to_int(s)
