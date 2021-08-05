from datetime import datetime



def log(func):
    def fun_file(*args, **kwargs):
        date = datetime.now()
        name = func.__name__
        result = func(*args, **kwargs)
        with open('result.txt', 'w') as file:
            file.write(f'{date}\n'
                       f'{name}\n'
                       f'{args, kwargs}\n'
                       f'{result}\n')
        return result
    return fun_file


@log
def get_sum(a, b):
    return a+b


if __name__ == '__main__':
    get_sum(5,3)