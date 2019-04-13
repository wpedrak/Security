import attr

@attr.s
class User:
    username = attr.ib()
    email = attr.ib()