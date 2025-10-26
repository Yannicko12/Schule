def inc(x):
    y = x+1
    return y
y = 0
b = inc(1)
print(y, b)

# Funktioniert auch, auch wenn es keinen Zusammenhang zwischen y und b gibt, weil y immer
# 0 ist und b immer 1+1=2 ist.