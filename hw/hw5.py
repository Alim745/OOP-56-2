def check_admin(is_admin: bool):
    def decorator(func):
        def wrapper():
            if is_admin:
                func()
            else:
                print("Доступ запрещен. Только для админов.")
        return wrapper
    return decorator

@check_admin(is_admin=True)
def delete_user():
    print("Пользователь удален.")

@check_admin(is_admin=False)
def delete_post():
    print("Пост удален.")

delete_user()
delete_post()