from abc import ABC, abstractmethod


class CannotChargeError(SystemError):
    pass


class CannotReverseError(SystemError):
    pass


class AbstractPayment(ABC):
    @abstractmethod
    def authorize_payment(self, user_id, amount, currency):
        pass

    @abstractmethod
    def charge_payment(self, user_id, amount, currency, merchant_id):
        pass

    @abstractmethod
    def reverse_payment(self, user_id, amount, currency, merchant_id):
        pass


class MyNewPayment(AbstractPayment):

    def authorize_payment(self, user_id, amount, currency):
        return user_id < 100

    def charge_payment(self, user_id, amount, currency, merchant_id):
        if amount < 0 or amount > 1000:
            raise CannotChargeError(
                f"user_id {user_id}, amount {amount}, currency {currency}, merchant_id {merchant_id}")

        return 10

    def reverse_payment(self, user_id, amount, currency, merchant_id):
        if amount < 0 or amount > 1000:
            raise CannotReverseError(
                f"user_id {user_id}, amount {amount}, currency {currency}, merchant_id {merchant_id}")

        return 10


if __name__ == '__main__':
    mnp = MyNewPayment()
    print(mnp.authorize_payment(30, 50, 'usd'))
    print(mnp.charge_payment(50, 900, 'euro', 3))
    print(mnp.reverse_payment(30, 80, 'usd', 1))
    print(mnp.charge_payment(50, 1100, 'euro', 2))
