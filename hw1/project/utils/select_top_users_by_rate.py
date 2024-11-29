def select_top_users_by_rate(users: list, top_size: int) -> list:
    return sorted(users, key= lambda user: user.rate, reverse=True)[0:top_size]
