from abc import ABC, abstractmethod


class Payment(ABC):
    # this function must be implemented in all subclasses
    @abstractmethod
    def process_payment(self):
        pass


class CreditCardPayment(Payment):
    def process_payment(self):
        pass


class StripePayment(Payment):
    def process_payment(self):
        pass


class PayPalPayment(Payment):
    def process_payment(self):
        pass
