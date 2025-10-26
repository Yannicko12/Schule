def inc():
    global x
    x = x+1
    return x
x = 0
z = inc()
print(x, z)

# In diesem Beispiel wurde der Fehler des vorherigen Programms verbessert und es funktioniert.
# Man muss allerdings beachten, dass x nun auch verändert ist.