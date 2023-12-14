from django.test import TestCase

from order.factories import UserFactory, OrderFactory
from product.factories import ProductFactory


class OrderFactoryTestCase(TestCase):
    def test_order_factory(self):
        user = UserFactory()
        product1 = ProductFactory()
        product2 = ProductFactory()
        order_instance = OrderFactory(user=user, product=[product1, product2])

        self.assertEqual(order_instance.user, user)
        self.assertIn(product1, order_instance.product.all())
        self.assertIn(product2, order_instance.product.all())

