class Hello(object):

    def hello(self, name='world'):
        print(f'Hello, {name}')


class Person(object):

    def say(self, words='hello'):
        print('我说: %s' % words)

        