str_WLPT = "We like Python's turtles! "
str_fl = "for loop "
str_cnt = "count = "

for i in range(100):
    print(str_WLPT + str_fl + str_cnt + str(i + 1))

print("---------------------------")    # Seperater

x = 0
str_wl = "while loop "

while x < 100:
    print(str_WLPT + str_wl + str_cnt + str(x + 1))
    x += 1
