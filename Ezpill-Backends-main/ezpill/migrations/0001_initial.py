# Generated by Django 4.2.7 on 2023-12-01 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField(blank=True, db_column='Image_URL', null=True)),
                ('product_title', models.TextField(blank=True, db_column='Product_Title', null=True)),
                ('product_manufacture', models.TextField(blank=True, db_column='Product_Manufacture', null=True)),
                ('product_price', models.TextField(blank=True, db_column='Product_Price', null=True)),
                ('product_per_price', models.TextField(blank=True, db_column='Product_Per_Price', null=True)),
                ('product_usage', models.TextField(blank=True, db_column='Product_Usage', null=True)),
                ('product_precautions', models.TextField(blank=True, db_column='Product_Precautions', null=True)),
                ('product_ingredient_information', models.TextField(blank=True, db_column='Product_Ingredient_Information', null=True)),
                ('review', models.TextField(blank=True, db_column='Review', null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCalcium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField(blank=True, db_column='Image_URL', null=True)),
                ('product_title', models.TextField(blank=True, db_column='Product_Title', null=True)),
                ('product_manufacture', models.TextField(blank=True, db_column='Product_Manufacture', null=True)),
                ('product_price', models.BigIntegerField(blank=True, db_column='Product_Price', null=True)),
                ('product_per_price', models.BigIntegerField(blank=True, db_column='Product_Per_Price', null=True)),
                ('product_usage', models.TextField(blank=True, db_column='Product_Usage', null=True)),
                ('product_precautions', models.TextField(blank=True, db_column='Product_Precautions', null=True)),
                ('product_ingredient_information', models.TextField(blank=True, db_column='Product_Ingredient_Information', null=True)),
                ('review', models.TextField(blank=True, db_column='Review', null=True)),
            ],
            options={
                'db_table': 'product_calcium',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCollagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField(blank=True, db_column='Image_URL', null=True)),
                ('product_title', models.TextField(blank=True, db_column='Product_Title', null=True)),
                ('product_manufacture', models.TextField(blank=True, db_column='Product_Manufacture', null=True)),
                ('product_price', models.TextField(blank=True, db_column='Product_Price', null=True)),
                ('product_per_price', models.TextField(blank=True, db_column='Product_Per_Price', null=True)),
                ('product_usage', models.TextField(blank=True, db_column='Product_Usage', null=True)),
                ('product_precautions', models.TextField(blank=True, db_column='Product_Precautions', null=True)),
                ('product_ingredient_information', models.TextField(blank=True, db_column='Product_Ingredient_Information', null=True)),
                ('review', models.TextField(blank=True, db_column='Review', null=True)),
            ],
            options={
                'db_table': 'product_collagen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductFolicAcid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField(blank=True, db_column='Image_URL', null=True)),
                ('product_title', models.TextField(blank=True, db_column='Product_Title', null=True)),
                ('product_manufacture', models.TextField(blank=True, db_column='Product_Manufacture', null=True)),
                ('product_price', models.TextField(blank=True, db_column='Product_Price', null=True)),
                ('product_per_price', models.TextField(blank=True, db_column='Product_Per_Price', null=True)),
                ('product_usage', models.TextField(blank=True, db_column='Product_Usage', null=True)),
                ('product_precautions', models.TextField(blank=True, db_column='Product_Precautions', null=True)),
                ('product_ingredient_information', models.TextField(blank=True, db_column='Product_Ingredient_Information', null=True)),
                ('review', models.TextField(blank=True, db_column='Review', null=True)),
            ],
            options={
                'db_table': 'product_folic_acid',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductIron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField(blank=True, db_column='Image_URL', null=True)),
                ('product_title', models.TextField(blank=True, db_column='Product_Title', null=True)),
                ('product_manufacture', models.TextField(blank=True, db_column='Product_Manufacture', null=True)),
                ('product_price', models.TextField(blank=True, db_column='Product_Price', null=True)),
                ('product_per_price', models.TextField(blank=True, db_column='Product_Per_Price', null=True)),
                ('product_usage', models.TextField(blank=True, db_column='Product_Usage', null=True)),
                ('product_precautions', models.TextField(blank=True, db_column='Product_Precautions', null=True)),
                ('product_ingredient_information', models.TextField(blank=True, db_column='Product_Ingredient_Information', null=True)),
                ('review', models.TextField(blank=True, db_column='Review', null=True)),
            ],
            options={
                'db_table': 'product_iron',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductLutein',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField(blank=True, db_column='Image_URL', null=True)),
                ('product_title', models.TextField(blank=True, db_column='Product_Title', null=True)),
                ('product_manufacture', models.TextField(blank=True, db_column='Product_Manufacture', null=True)),
                ('product_price', models.TextField(blank=True, db_column='Product_Price', null=True)),
                ('product_per_price', models.TextField(blank=True, db_column='Product_Per_Price', null=True)),
                ('product_usage', models.TextField(blank=True, db_column='Product_Usage', null=True)),
                ('product_precautions', models.TextField(blank=True, db_column='Product_Precautions', null=True)),
                ('product_ingredient_information', models.TextField(blank=True, db_column='Product_Ingredient_Information', null=True)),
                ('review', models.TextField(blank=True, db_column='Review', null=True)),
            ],
            options={
                'db_table': 'product_lutein',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductMagnesium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField(blank=True, db_column='Image_URL', null=True)),
                ('product_title', models.TextField(blank=True, db_column='Product_Title', null=True)),
                ('product_manufacture', models.TextField(blank=True, db_column='Product_Manufacture', null=True)),
                ('product_price', models.TextField(blank=True, db_column='Product_Price', null=True)),
                ('product_per_price', models.TextField(blank=True, db_column='Product_Per_Price', null=True)),
                ('product_usage', models.TextField(blank=True, db_column='Product_Usage', null=True)),
                ('product_precautions', models.TextField(blank=True, db_column='Product_Precautions', null=True)),
                ('product_ingredient_information', models.TextField(blank=True, db_column='Product_Ingredient_Information', null=True)),
                ('review', models.TextField(blank=True, db_column='Review', null=True)),
            ],
            options={
                'db_table': 'product_magnesium',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductOmega3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField(blank=True, db_column='Image_URL', null=True)),
                ('product_title', models.TextField(blank=True, db_column='Product_Title', null=True)),
                ('product_manufacture', models.TextField(blank=True, db_column='Product_Manufacture', null=True)),
                ('product_price', models.TextField(blank=True, db_column='Product_Price', null=True)),
                ('product_per_price', models.TextField(blank=True, db_column='Product_Per_Price', null=True)),
                ('product_usage', models.TextField(blank=True, db_column='Product_Usage', null=True)),
                ('product_precautions', models.TextField(blank=True, db_column='Product_Precautions', null=True)),
                ('product_ingredient_information', models.TextField(blank=True, db_column='Product_Ingredient_Information', null=True)),
                ('review', models.TextField(blank=True, db_column='Review', null=True)),
            ],
            options={
                'db_table': 'product_omega_3',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductProbiotic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField(blank=True, db_column='Image_URL', null=True)),
                ('product_title', models.TextField(blank=True, db_column='Product_Title', null=True)),
                ('product_manufacture', models.TextField(blank=True, db_column='Product_Manufacture', null=True)),
                ('product_price', models.TextField(blank=True, db_column='Product_Price', null=True)),
                ('product_per_price', models.TextField(blank=True, db_column='Product_Per_Price', null=True)),
                ('product_usage', models.TextField(blank=True, db_column='Product_Usage', null=True)),
                ('product_precautions', models.TextField(blank=True, db_column='Product_Precautions', null=True)),
                ('product_ingredient_information', models.TextField(blank=True, db_column='Product_Ingredient_Information', null=True)),
                ('review', models.TextField(blank=True, db_column='Review', null=True)),
            ],
            options={
                'db_table': 'product_probiotic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductVitaminB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField(blank=True, db_column='Image_URL', null=True)),
                ('product_title', models.TextField(blank=True, db_column='Product_Title', null=True)),
                ('product_manufacture', models.TextField(blank=True, db_column='Product_Manufacture', null=True)),
                ('product_price', models.BigIntegerField(blank=True, db_column='Product_Price', null=True)),
                ('product_per_price', models.BigIntegerField(blank=True, db_column='Product_Per_Price', null=True)),
                ('product_usage', models.TextField(blank=True, db_column='Product_Usage', null=True)),
                ('product_precautions', models.TextField(blank=True, db_column='Product_Precautions', null=True)),
                ('product_ingredient_information', models.TextField(blank=True, db_column='Product_Ingredient_Information', null=True)),
                ('review', models.TextField(blank=True, db_column='Review', null=True)),
            ],
            options={
                'db_table': 'product_Vitamin_B',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductVitaminD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField(blank=True, db_column='Image_URL', null=True)),
                ('product_title', models.TextField(blank=True, db_column='Product_Title', null=True)),
                ('product_manufacture', models.TextField(blank=True, db_column='Product_Manufacture', null=True)),
                ('product_price', models.TextField(blank=True, db_column='Product_Price', null=True)),
                ('product_per_price', models.TextField(blank=True, db_column='Product_Per_Price', null=True)),
                ('product_usage', models.TextField(blank=True, db_column='Product_Usage', null=True)),
                ('product_precautions', models.TextField(blank=True, db_column='Product_Precautions', null=True)),
                ('product_ingredient_information', models.TextField(blank=True, db_column='Product_Ingredient_Information', null=True)),
                ('review', models.TextField(blank=True, db_column='Review', null=True)),
            ],
            options={
                'db_table': 'product_Vitamin_D',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('survey_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('preg_week', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('bmi', models.IntegerField(blank=True, null=True)),
                ('medication', models.CharField(blank=True, max_length=20, null=True)),
                ('sea_food_allergy', models.IntegerField(blank=True, null=True)),
                ('probiotic_allergy', models.IntegerField(blank=True, null=True)),
                ('collagen_allergy', models.IntegerField(blank=True, null=True)),
                ('lutein_allergy', models.IntegerField(blank=True, null=True)),
                ('diabetes', models.IntegerField(blank=True, null=True)),
                ('high_blood_pressure', models.IntegerField(blank=True, null=True)),
                ('heart_disease', models.IntegerField(blank=True, null=True)),
                ('liver_cirrhosis', models.IntegerField(blank=True, null=True)),
                ('rheumatoid_arthritis', models.IntegerField(blank=True, null=True)),
                ('obesity', models.IntegerField(blank=True, null=True)),
                ('digestive_issues', models.IntegerField(blank=True, null=True)),
                ('muscle_twitching', models.IntegerField(blank=True, null=True)),
                ('eye_fatigue', models.IntegerField(blank=True, null=True)),
                ('skin_condition', models.IntegerField(blank=True, null=True)),
                ('feel_down', models.IntegerField(blank=True, null=True)),
                ('pill_preference', models.CharField(blank=True, max_length=20, null=True)),
                ('budget', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'survey',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
