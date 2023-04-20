from pathlib import Path

p1 = Path("C:/Users/shari/Desktop/Automate Eerything with Python/Intro to Pathlib/abc.txt")
print(type(p1))


print(p1.name)
print(p1.stem)
print(p1.suffix)


p2 = Path("C:/Users/shari/Desktop/Automate Eerything with Python/Intro to Pathlib")
for item in p2.iterdir():
    print(item)


