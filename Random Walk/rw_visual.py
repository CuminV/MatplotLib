import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    points_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    
    
    keep_runing = input('Make another walk? (y/n): ')
    if keep_runing == 'n':
        break