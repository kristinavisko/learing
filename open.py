
f = open("/home/kristina/projects/learning/kiki.txt", "w+")
f.write("Some text in new txt file")
f.seek(0)
x = f.read()
print (x)
