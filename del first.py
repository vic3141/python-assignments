str1 = str(input("Enter a sentence: "))
result = ""
ch_to_remove = str(input("input a char: "))
occurred_flag = False
# iterate over each character in s
for ch in str1:
    if ch == ch_to_remove and occurred_flag == False:
        occurred_flag = True
        continue
    else:
        result += ch
# display the resulting string
print(result)
