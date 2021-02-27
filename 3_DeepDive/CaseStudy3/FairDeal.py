class Customer:
    def __init__(self, title, first_nm, last_nm, b_listed):
        self.title = title
        self.first_name = first_nm
        self.last_name = last_nm
        self.b_listed = b_listed

    def is_black_listed(self):
        return self.b_listed

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_title(self):
        return self.title


class CustomerNotAllowedException(Exception):
    def __init__(self, customer):
        pass


def create_order(customer):
    if customer.is_black_listed():
        raise CustomerNotAllowedException(customer)



