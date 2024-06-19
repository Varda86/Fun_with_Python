print("\nLET'S TRANSLATE A ROMAN NUMBER IN ARABIC NUMBER!!!\n")
print("This code considers that the user can make a mistake while inserting the roman number\n")

'''LIST OF FUNCTIONS'''
#This function transform the string of roman numbers in a list of arabic numbers
#N.B. This function tells us if one letter of the string is not a roman number
def create_list():
    roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D': 500, 'M' : 1000}
    list_arabic = []
    for letter in roman_string:
        if letter in roman.keys():
            list_arabic.append(roman[letter])
        else:
            print("The inserted number contains symbols that do not represent any Roman number\n")
            exit()
    return(list_arabic)

#This function help us to recognise any wrong transcription of the Roman number
def find_mistake(list_num):
    length = len(list_num)
    for n in range(length-3):
        if list_num[n] == list_num[n+3]:
            print("Error!! There are too many equal symbols!!! Example: IIII\n")
            exit()
    if length >=3:
        for n in range(length-1, 1, -1):
            if list_num[n] > list_num[n-2]:
                print("Error!! There are too many smaller symbols before a bigger symbol!!! Example: IIX\n")
                exit()
    return(list_num)

#Finally this function tells us the arabic value of the roman number
def roman_to_arabic(list_num):
    length = len(list_num)
    arabic = 0
    for n in range(length-1):
        if list_num[n] >= list_num[n+1]:
            arabic += (list_num[n])
        else:
             list_num[n+1] -= list_num[n]
    arabic +=list_num[-1]
    return arabic
'''END OF LIST OF FUNCTIONS'''


#And this is the main function
roman_string = input("Insert a roman number--> ").upper()
print(f"\nThe translation in arabic numers of the Roman number {roman_string} is {roman_to_arabic(find_mistake(create_list()))}\n")
