# user authentication check

def is_user_auth():
    return True  # change to False


def chech_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_auth():
            print('User is authenticated!')
            return fn(*args, **kwargs)
        else:
            raise Exception('User is not authenticated.')

    return wrapper


@chech_user_auth
def do_task():
    # perform task if user is authenticated
    print('Task done.')


try:
    do_task()
except Exception as e:
    print(e)
