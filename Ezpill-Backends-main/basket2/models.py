from django.db import models

class Basket2(models.Model):
    id = models.BigAutoField(primary_key=True)  # 기본 키로 BigAutoField 사용
    firebase_uid = models.CharField(max_length=255)  # 고유 필드로 설정
    product_id = models.CharField(max_length=255)
    product_title = models.CharField(db_column='Product_Title', max_length=1024)
    product_per_price = models.CharField(db_column='Product_Per_Price', max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basket2'
