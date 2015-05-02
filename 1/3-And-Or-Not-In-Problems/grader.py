points = input("Enter student score: ")
points = int(points)


if points <= 50:
    print("Слаб 2")
elif points >= 51 and points <= 60:
    print("Среден 3")
elif points >= 61 and points <= 70:
    print("Добър 4")
elif points >= 71 and points <= 80:
    print("Много Добър 5")
elif points >= 81 and points <= 99:
    print("Отличен 6")
elif points == 100:
    print("Много Отличен 7")
