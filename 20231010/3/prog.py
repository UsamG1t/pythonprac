n = m = 0
air = water = 0

while (s := input()):
    n = len(s)
    m += 1
    if s[1] == '.':
        air += n-2
    elif s[1] == '~':
        water += n-2

water_flag = 0

print('#' * m)
for i in range(1, n-1):
    if air >= m-2:
        print('#', '.'*(m-2), '#', sep = '')
        air -= m-2
    elif water_flag == 0:
        water_flag = i

    if water_flag:
        if water > 0:
            print('#', '~'*(m-2), '#', sep = '')
            water -= m-2
print('#' * m)

air = (m-2) * (water_flag - 1)
water = (m-2) * (n-1 - water_flag)

print(f"{'.' * round(20 * air / max(air, water)):<20}", f"{(str(air) + '/' + str(air + water)):>5}")
print(f"{'~' * round(20 * water / max(air, water)):<20}", f"{(str(water) + '/' + str(air + water)):>5}")

