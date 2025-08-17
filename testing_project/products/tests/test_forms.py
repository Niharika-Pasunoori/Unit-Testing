from django.test import TestCase,override_settings
from django.urls import reverse
from products.models import Product

class ProductFormTest(TestCase):
    def test_create_product_when_submitting_valid_form(self):
        """Test that form submission with invalid data does not create a product."""
        form_data={
            'name':'Tablet',
            'price':299.99,
            'stock_count':50
        }
        response=self.client.post(reverse('products'),data=form_data)

        # Check that the product was created and we were redirected
        self.assertEqual(response.status_code,302)
        self.assertTrue(Product.objects.filter(name='Tablet').exists())

    @override_settings(MAINTENANCE_MODE=False)
    def test_dont_create_product_when_submitting_invalid_form(self):
        """Test form submission with invalid data does not create a product."""
        form_data={
            'name':'',
            'price':-50.00,
            'stock_count': -5
        }
        response=self.client.post(reverse('products'),data=form_data)
        self.assertEqual(response.status_code,200)
        self.assertTrue("form" in response.context)

        # Check that we get a 200 status (stay on the page to correct errors)
        self.assertEqual(response.status_code,200)

        form=response.context['form']
        self.assertFormError(form,'name','This field is required')
        self.assertFormError(form,'price','Price cannot be negative')
        self.assertFormError(form,'stock_count','Stock count cannot be negative')

        # Ensure no product was created in the database
        self.assertFalse(Product.objects.exists())

