def inc():
    y = x+1
    return y
x = 0
z = inc()
print(x, z)

# Dieses Beispiel funktioniert auch so wie das vorherige, 
# nur das diesmal inc ohne lokale Variable x arbeitet, sondern mit der globalen Variable.