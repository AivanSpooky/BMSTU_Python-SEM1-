import matplotlib.pyplot as plt

x = [6, 12, 20, 7, 5, 5]

languages = ['Matlab', 'Java', 'Python', 'C', 'C++', 'Other']

plt.figure(figsize=(10,10))

explode = [0, 0, 0, 0.1, 0, 0]

plt.pie(x, labels = languages, explode=explode, autopct='%1.1f%%', shadow=False)
plt.title('Circle diagram')

plt.show()
