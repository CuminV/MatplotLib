import matplotlib.pyplot as plt

x_value = list(range(1,5001))
y_value = [x**3 for x in x_value]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s=10)

ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()