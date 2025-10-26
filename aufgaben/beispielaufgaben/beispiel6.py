def inc():
    y = x+1
    return y
x = 0
z = inc()
print(x, y, z)

# Dieses Beispiel ist identisch zu Beispiel5, nur wird diesmal die y-Variable mit ausgegeben,
# die allerdings nur lokal ist, daher wird sie nicht gefunden und das Programm ist nicht lauffähig.
