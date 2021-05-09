from numpy import split


split_message = 'stats south africa'


split_message = split_message.lower().title().split()

output = ''
for i in range(len(split_message)):
    print(split_message[i])
    if i != 0:
        output += split_message[i] + ' '

country_name = output.strip()

print(country_name)
