def story(**kwds):
    return 'Once upon a time, there was a ' \
           '{job} called {name}.'.format_map(kwds)


print(story(job='king', name='Gumby'))
params = {'job': 'language', 'name': 'python'}
print(story(**params))


def another_story(**kwargs):
    for key, value in kwargs.items():
        print('Once upon a time, there was a ' \
              f'{key} called {value}.'.format_map(kwargs))


another_story(King="Solomon",
              Prince="Absalom")


def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    print(pow(x, y))


power(2, 3, 6, 7, 4, 4)
power(1, 2, 'Hello World')
power(1, 2, {'name':'emeka'})
