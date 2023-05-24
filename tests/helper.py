from faker import Faker


def get_fake_email():
    return Faker().email()


def get_fake_name():
    return Faker().name()


def get_fake_password():
    return Faker().password(6, 10)
