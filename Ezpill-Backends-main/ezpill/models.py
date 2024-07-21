from django.db import models


class Basket(models.Model):
    basket_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Survey', models.DO_NOTHING, blank=True, null=True)
    pill_1 = models.CharField(max_length=45, blank=True, null=True)
    pill_2 = models.CharField(max_length=45, blank=True, null=True)
    pill_3 = models.CharField(max_length=45, blank=True, null=True)
    pill_4 = models.CharField(max_length=45, blank=True, null=True)
    pill_5 = models.CharField(max_length=45, blank=True, null=True)
    pill_6 = models.CharField(max_length=45, blank=True, null=True)
    pill_7 = models.CharField(max_length=45, blank=True, null=True)
    pill_8 = models.CharField(max_length=45, blank=True, null=True)
    pill_9 = models.CharField(max_length=45, blank=True, null=True)
    pill_10 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basket'


class Basket2(models.Model):
    firebase_uid = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)
    product_title = models.CharField(db_column='Product_Title', max_length=1024)  # Field name made lowercase.
    product_per_price = models.CharField(db_column='Product_Per_Price', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basket2'

# Create your models here.
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


class ProductVitaminB(models.Model):
    image_url = models.TextField(db_column='Image_URL', blank=True, null=True)  # Field name made lowercase.
    product_title = models.TextField(db_column='Product_Title', blank=True, null=True)  # Field name made lowercase.
    product_manufacture = models.TextField(db_column='Product_Manufacture', blank=True, null=True)  # Field name made lowercase.
    product_price = models.BigIntegerField(db_column='Product_Price', blank=True, null=True)  # Field name made lowercase.
    product_per_price = models.BigIntegerField(db_column='Product_Per_Price', blank=True, null=True)  # Field name made lowercase.
    product_usage = models.TextField(db_column='Product_Usage', blank=True, null=True)  # Field name made lowercase.
    product_precautions = models.TextField(db_column='Product_Precautions', blank=True, null=True)  # Field name made lowercase.
    product_ingredient_information = models.TextField(db_column='Product_Ingredient_Information', blank=True, null=True)  # Field name made lowercase.
    review = models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(blank=True, null=True)
    vitamin_b_id = models.AutoField(db_column='Vitamin_B_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product_Vitamin_B'


class ProductVitaminD(models.Model):
    image_url = models.TextField(db_column='Image_URL', blank=True, null=True)  # Field name made lowercase.
    product_title = models.TextField(db_column='Product_Title', blank=True, null=True)  # Field name made lowercase.
    product_manufacture = models.TextField(db_column='Product_Manufacture', blank=True, null=True)  # Field name made lowercase.
    product_price = models.TextField(db_column='Product_Price', blank=True, null=True)  # Field name made lowercase.
    product_per_price = models.TextField(db_column='Product_Per_Price', blank=True, null=True)  # Field name made lowercase.
    product_usage = models.TextField(db_column='Product_Usage', blank=True, null=True)  # Field name made lowercase.
    product_precautions = models.TextField(db_column='Product_Precautions', blank=True, null=True)  # Field name made lowercase.
    product_ingredient_information = models.TextField(db_column='Product_Ingredient_Information', blank=True, null=True)  # Field name made lowercase.
    review = models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(blank=True, null=True)
    vitamin_d_id = models.AutoField(db_column='Vitamin_D_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product_Vitamin_D'


class ProductCalcium(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    calcium = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)
    product_title = models.TextField(db_column='Product_Title', blank=True, null=True)  # Field name made lowercase.
    image_url = models.TextField(db_column='Image_URL', blank=True, null=True)  # Field name made lowercase.
    product_manufacture = models.TextField(db_column='Product_Manufacture', blank=True, null=True)  # Field name made lowercase.
    product_price = models.BigIntegerField(db_column='Product_Price', blank=True, null=True)  # Field name made lowercase.
    product_per_price = models.BigIntegerField(db_column='Product_Per_Price', blank=True, null=True)  # Field name made lowercase.
    product_usage = models.TextField(db_column='Product_Usage', blank=True, null=True)  # Field name made lowercase.
    product_precautions = models.TextField(db_column='Product_Precautions', blank=True, null=True)  # Field name made lowercase.
    product_ingredient_information = models.TextField(db_column='Product_Ingredient_Information', blank=True, null=True)  # Field name made lowercase.
    review = models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product_calcium'


class ProductCollagen(models.Model):
    image_url = models.TextField(db_column='Image_URL', blank=True, null=True)  # Field name made lowercase.
    product_title = models.TextField(db_column='Product_Title', blank=True, null=True)  # Field name made lowercase.
    product_manufacture = models.TextField(db_column='Product_Manufacture', blank=True, null=True)  # Field name made lowercase.
    product_price = models.TextField(db_column='Product_Price', blank=True, null=True)  # Field name made lowercase.
    product_per_price = models.TextField(db_column='Product_Per_Price', blank=True, null=True)  # Field name made lowercase.
    product_usage = models.TextField(db_column='Product_Usage', blank=True, null=True)  # Field name made lowercase.
    product_precautions = models.TextField(db_column='Product_Precautions', blank=True, null=True)  # Field name made lowercase.
    product_ingredient_information = models.TextField(db_column='Product_Ingredient_Information', blank=True, null=True)  # Field name made lowercase.
    review = models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(blank=True, null=True)
    collagen_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'product_collagen'


class ProductFolicAcid(models.Model):
    image_url = models.TextField(db_column='Image_URL', blank=True, null=True)  # Field name made lowercase.
    product_title = models.TextField(db_column='Product_Title', blank=True, null=True)  # Field name made lowercase.
    product_manufacture = models.TextField(db_column='Product_Manufacture', blank=True, null=True)  # Field name made lowercase.
    product_price = models.TextField(db_column='Product_Price', blank=True, null=True)  # Field name made lowercase.
    product_per_price = models.TextField(db_column='Product_Per_Price', blank=True, null=True)  # Field name made lowercase.
    product_usage = models.TextField(db_column='Product_Usage', blank=True, null=True)  # Field name made lowercase.
    product_precautions = models.TextField(db_column='Product_Precautions', blank=True, null=True)  # Field name made lowercase.
    product_ingredient_information = models.TextField(db_column='Product_Ingredient_Information', blank=True, null=True)  # Field name made lowercase.
    review = models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(blank=True, null=True)
    folic_acid_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'product_folic_acid'


class ProductIron(models.Model):
    image_url = models.TextField(db_column='Image_URL', blank=True, null=True)  # Field name made lowercase.
    product_title = models.TextField(db_column='Product_Title', blank=True, null=True)  # Field name made lowercase.
    product_manufacture = models.TextField(db_column='Product_Manufacture', blank=True, null=True)  # Field name made lowercase.
    product_price = models.TextField(db_column='Product_Price', blank=True, null=True)  # Field name made lowercase.
    product_per_price = models.TextField(db_column='Product_Per_Price', blank=True, null=True)  # Field name made lowercase.
    product_usage = models.TextField(db_column='Product_Usage', blank=True, null=True)  # Field name made lowercase.
    product_precautions = models.TextField(db_column='Product_Precautions', blank=True, null=True)  # Field name made lowercase.
    product_ingredient_information = models.TextField(db_column='Product_Ingredient_Information', blank=True, null=True)  # Field name made lowercase.
    review = models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(blank=True, null=True)
    iron_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'product_iron'


class ProductLutein(models.Model):
    image_url = models.TextField(db_column='Image_URL', blank=True, null=True)  # Field name made lowercase.
    product_title = models.TextField(db_column='Product_Title', blank=True, null=True)  # Field name made lowercase.
    product_manufacture = models.TextField(db_column='Product_Manufacture', blank=True, null=True)  # Field name made lowercase.
    product_price = models.TextField(db_column='Product_Price', blank=True, null=True)  # Field name made lowercase.
    product_per_price = models.TextField(db_column='Product_Per_Price', blank=True, null=True)  # Field name made lowercase.
    product_usage = models.TextField(db_column='Product_Usage', blank=True, null=True)  # Field name made lowercase.
    product_precautions = models.TextField(db_column='Product_Precautions', blank=True, null=True)  # Field name made lowercase.
    product_ingredient_information = models.TextField(db_column='Product_Ingredient_Information', blank=True, null=True)  # Field name made lowercase.
    review = models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(blank=True, null=True)
    lutein_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'product_lutein'


class ProductMagnesium(models.Model):
    image_url = models.TextField(db_column='Image_URL', blank=True, null=True)  # Field name made lowercase.
    product_title = models.TextField(db_column='Product_Title', blank=True, null=True)  # Field name made lowercase.
    product_manufacture = models.TextField(db_column='Product_Manufacture', blank=True, null=True)  # Field name made lowercase.
    product_price = models.TextField(db_column='Product_Price', blank=True, null=True)  # Field name made lowercase.
    product_per_price = models.TextField(db_column='Product_Per_Price', blank=True, null=True)  # Field name made lowercase.
    product_usage = models.TextField(db_column='Product_Usage', blank=True, null=True)  # Field name made lowercase.
    product_precautions = models.TextField(db_column='Product_Precautions', blank=True, null=True)  # Field name made lowercase.
    product_ingredient_information = models.TextField(db_column='Product_Ingredient_Information', blank=True, null=True)  # Field name made lowercase.
    review = models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(blank=True, null=True)
    magnesium_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'product_magnesium'


class ProductOmega3(models.Model):
    image_url = models.TextField(db_column='Image_URL', blank=True, null=True)  # Field name made lowercase.
    product_title = models.TextField(db_column='Product_Title', blank=True, null=True)  # Field name made lowercase.
    product_manufacture = models.TextField(db_column='Product_Manufacture', blank=True, null=True)  # Field name made lowercase.
    product_price = models.TextField(db_column='Product_Price', blank=True, null=True)  # Field name made lowercase.
    product_per_price = models.TextField(db_column='Product_Per_Price', blank=True, null=True)  # Field name made lowercase.
    product_usage = models.TextField(db_column='Product_Usage', blank=True, null=True)  # Field name made lowercase.
    product_precautions = models.TextField(db_column='Product_Precautions', blank=True, null=True)  # Field name made lowercase.
    product_ingredient_information = models.TextField(db_column='Product_Ingredient_Information', blank=True, null=True)  # Field name made lowercase.
    review = models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(blank=True, null=True)
    omega_3_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'product_omega_3'


class ProductProbiotic(models.Model):
    image_url = models.TextField(db_column='Image_URL', blank=True, null=True)  # Field name made lowercase.
    product_title = models.TextField(db_column='Product_Title', blank=True, null=True)  # Field name made lowercase.
    product_manufacture = models.TextField(db_column='Product_Manufacture', blank=True, null=True)  # Field name made lowercase.
    product_price = models.TextField(db_column='Product_Price', blank=True, null=True)  # Field name made lowercase.
    product_per_price = models.TextField(db_column='Product_Per_Price', blank=True, null=True)  # Field name made lowercase.
    product_usage = models.TextField(db_column='Product_Usage', blank=True, null=True)  # Field name made lowercase.
    product_precautions = models.TextField(db_column='Product_Precautions', blank=True, null=True)  # Field name made lowercase.
    product_ingredient_information = models.TextField(db_column='Product_Ingredient_Information', blank=True, null=True)  # Field name made lowercase.
    review = models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(blank=True, null=True)
    probiotic_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'product_probiotic'


class Survey(models.Model):
    survey_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    preg_week = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    bmi = models.IntegerField(blank=True, null=True)
    medication = models.CharField(max_length=20, blank=True, null=True)
    sea_food_allergy = models.IntegerField(blank=True, null=True)
    probiotic_allergy = models.IntegerField(blank=True, null=True)
    collagen_allergy = models.IntegerField(blank=True, null=True)
    lutein_allergy = models.IntegerField(blank=True, null=True)
    diabetes = models.IntegerField(blank=True, null=True)
    high_blood_pressure = models.IntegerField(blank=True, null=True)
    heart_disease = models.IntegerField(blank=True, null=True)
    liver_cirrhosis = models.IntegerField(blank=True, null=True)
    rheumatoid_arthritis = models.IntegerField(blank=True, null=True)
    obesity = models.IntegerField(blank=True, null=True)
    digestive_issues = models.IntegerField(blank=True, null=True)
    muscle_twitching = models.IntegerField(blank=True, null=True)
    eye_fatigue = models.IntegerField(blank=True, null=True)
    skin_condition = models.IntegerField(blank=True, null=True)
    feel_down = models.IntegerField(blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    phone = models.CharField(unique=True, max_length=20)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

class Surveyresponses(models.Model):
    firebase_uid = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    pregnancy_week = models.IntegerField(blank=True, null=True)
    supplements = models.TextField(blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    chronic_diseases = models.TextField(blank=True, null=True)
    health_concerns = models.TextField(blank=True, null=True)
    investment = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SurveyResponses'