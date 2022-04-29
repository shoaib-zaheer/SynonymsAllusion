import random

observations = ['Real', 'Fake']
flowers = ['Iris setosa', 'Iris virginica', 'Iris versicolor']

with open('DB_data.dat', 'w') as f:
    for _ in range(20):
        observation = random.choice(observations)
        flower = random.choice(flowers)
        sepal_width = random.random()
        sepal_length = random.random()
        petal_width = random.random()
        petal_length = random.random()

        f.write('{} {} {:.3f} {:.3f} {:.3f} {:.3f}\n'.format(
            observation,
            flower,
            sepal_length,
            sepal_width,
            petal_length,
            petal_width))

with open('DB_data.dat', 'r') as f:
    line = f.readline()
    data = []
    while line:
        data.append(line.split(' '))
        line = f.readline()
print(data)