def inc():
    x = x+1
    return x
x = 0
z = inc()
print(x, z)

# In dieser Funktion denkt er, dass x lokal ist, obwohl es keines gibt. 
# Deswegen ist das Programm nicht lauffähig. 
# Man müsste global x davorschreiben, damit er weiß, was gemeint ist.
