# given a string with list of fahrenheit temperature 
# Finding average using length and average

week_temp_f = "75.1,77.7,83.2,82.8,81.0,79.3,88.4"

temp_list = week_temp_f.split(",")
sum_temp = 0
num_temp = 0
for i in temp_list:
    t = float(t)
    sum_temp += t
    num_temp += 1

avg_temp = sum_temp/num_temp



# Code to create a list of word lengths

original_str = "The quick brown fox jumped over the lazy rabbit"
word_list = []
temp_list = original_str.split(" ")
num_words = len(original_str)

for i in temp_list:
    word_list.append((len(i)))
print(word_list)



# Create an empty string assign to variable lett 

lett = ""
for i in range(7):
    lett += 'b'
print(lett, end='')