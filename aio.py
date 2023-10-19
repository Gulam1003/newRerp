"""print("hello world")
f = open("demofile.text","w")
f.write("gulam\n")
print("written succesfully")
f.close()"""

with open("demofile.text") as f:
    text=f.read()
    print(text)
    print(f.tell())
    print(f.seek(3))
    print(f.tell())
    print("my name is gulam ansari")
    f.close()