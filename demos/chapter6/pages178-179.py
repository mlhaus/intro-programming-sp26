movies = [
    ["The Holy Grail", 1975, 9.99],
    ["Life of Brian", 1979, 12.30],
    ["The Meaning of Life", 1983, 7.50]
]

print(movies[0][0])
print(movies[1][0])
print(movies[2][0])

print(movies[0][1])
print(movies[1][1])
print(movies[2][1])

print(movies[0][2])
print(movies[1][2])
print(movies[2][2])

print("| Title | Year | Price |")
for movie in movies:
    print("| ", end="")
    for col in movie:
        print(str(col) + " | ", end="")
    print()