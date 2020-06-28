import pandas as pd
from datetime import datetime
from django.shortcuts import render, redirect
from products.models import Product
from sellers.models import Seller
from sellers.models import Seller_Price
from .crawl_website import crawl_website


def crawl_prices(request):
    if request.user.is_superuser:
        products = Product.objects.order_by("-date_added")
    else:
        products = Product.objects.order_by("-date_added").filter(
            client_id=request.user
        )

    for product in products:

        # Crawl Website
        if product.sku:
            df = crawl_website(product, xpath_dict)
            for i in range(len(df)):
                row = df.iloc[i]

                # Create Seller Object if it doesn't exist
                seller_obj, created = Seller.objects.get_or_create(
                    name=row["Seller_Name"]
                )
                # Update Previous Seller_Product records 'current' to False
                Seller_Price.objects.all().filter(
                    seller_id=seller_obj, product_id=product
                ).update(latest_update=False)

                # Record screenshot if there is a violation
                if row["MAP_Violation"]:
                    seller_price_obj = Seller_Price.objects.create(
                        seller_id=seller_obj,
                        product_id=product,
                        date_reported=row["Time_Stamp"],
                        url=row["Seller_URL"],
                        seller_price=row["Current_Price"],
                        discount=row["Discount"],
                        violation=row["MAP_Violation"],
                        violation_snapshot=row["Screenshot"],
                    )
                else:
                    seller_price_obj = Seller_Price.objects.create(
                        seller_id=seller_obj,
                        product_id=product,
                        date_reported=row["Time_Stamp"],
                        url=row["Seller_URL"],
                        seller_price=row["Current_Price"],
                        discount=row["Discount"],
                        violation=row["MAP_Violation"],
                    )
    return redirect("/admin")


from django.views.generic import View
from django.utils import timezone
from .models import *


# This passes database objects to html template for reports
class Pdf(View):
    def get(self, request):
        seller_price = Seller_Price.objects.order_by("-date_reported").filter(
            product_id__client_id=request.user, latest_update=True
        )
        today = timezone.now()
        params = {"today": today, "seller_price": seller_price, "request": request}
