from django.db import models


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    image_url = models.TextField(db_column='Image_URL', blank=True, null=True)  # Field name made lowercase.
    product_title = models.TextField(db_column='Product_Title', blank=True, null=True)  # Field name made lowercase.
    product_manufacture = models.TextField(db_column='Product_Manufacture', blank=True, null=True)  # Field name made lowercase.
    product_price = models.TextField(db_column='Product_Price', blank=True, null=True)  # Field name made lowercase.
    product_per_price = models.TextField(db_column='Product_Per_Price', blank=True, null=True)  # Field name made lowercase.
    product_usage = models.TextField(db_column='Product_Usage', blank=True, null=True)  # Field name made lowercase.
    product_precautions = models.TextField(db_column='Product_Precautions', blank=True, null=True)  # Field name made lowercase.
    product_ingredient_information = models.TextField(db_column='Product_Ingredient_Information', blank=True, null=True)  # Field name made lowercase.
    review = models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'
