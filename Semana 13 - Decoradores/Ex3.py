from datetime import date


class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()

        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )


def validate_adult_user(func):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError("User must be at least 18 years old")

        return func(user, *args, **kwargs)

    return wrapper


@validate_adult_user
def buy_product(user, product_name):
    print(f"User with age {user.age} bought {product_name}")


adult_user = User(date(1995, 5, 20))
minor_user = User(date(2010, 8, 15))


buy_product(adult_user, "Alcohol")

