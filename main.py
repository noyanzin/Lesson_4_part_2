import numpy as np
x = [1, 2, 9, 10, 10]


def RSS(x):
    a = np.average(x)
    d = (x - a) ** 2
    return sum(d)



def split(x):
    best_rss = 1e10
    best_values_left = []
    best_values_right = []
    print(f'start split {x}')
    rss_before = RSS(x)
    print(f'rss_before={rss_before}')
    for i in range(1, len(x)):
        values_left = []
        for i_left in range(0, i):
            values_left.append(x[i_left])
        values_right = []
        for i_right in range(i, len(x)):
            values_right.append(x[i_right])
        rss_left = RSS(values_left)
        rss_right = RSS(values_right)
        rss = rss_left + rss_right
        print(f'-> i={i}, '
              f'left={values_left}, '
              f'right={values_right}, '
              f'rss_left={rss_left}, '
              f'rss_right = {rss_right} '
              f'rss={rss}')
        if rss < best_rss:
            best_values_left = values_left
            best_values_right = values_right
            best_rss = rss
            best_y = x[i]
    print(f'best_rss = {best_rss}, '
          f'best_values_left = {best_values_left}, '
          f'best_values_right = {best_values_right}, '
          f'best_y={best_y}')
    print(f'end split {x}')
    print()
    if best_rss == 0:
        return
    split(best_values_left)
    split(best_values_right)


split(x)