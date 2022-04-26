from django import http
from django.urls import URLPattern, path
from .views import * 

urlpatterns = [
    # Color API URLs
    path('colors/', ColorView.as_view(http_method_names=["get","post"]), name='colors'),
    path('colors/<int:pk>/', ColorView.as_view(http_method_names=["get","post","delete"]), name='colors with pk'),
    # Brand API URLs
    path('brands/', BrandView.as_view(http_method_names=["get","post"]), name='brands'),
    path('brands/<int:pk>/', BrandView.as_view(http_method_names=["get","post","delete"]), name='brands with pk'),
    # Unites API URLs
    path('unites/', UnitesView.as_view(http_method_names=["get","post"]), name='unites'),
    path('unites/<int:pk>/', UnitesView.as_view(http_method_names=["get","post","delete"]), name='unites with pk'),
    # Currencies API URLs
    path('currencies/', CurrenciesView.as_view(http_method_names=["get","post"]), name='currencies'),
    path('currencies/<int:pk>/', CurrenciesView.as_view(http_method_names=["get","post","delete"]), name='currencies with pk'),
    # Categories API URLs
    path('categories/', CategoriesView.as_view(http_method_names=["get","post","put"]), name='categories'),
    path('categories/<int:pk>/', CategoriesView.as_view(http_method_names=["get","post","delete"]), name='categories with pk'),
    # Products API URLs
    path('products/', ProductsView.as_view(http_method_names=["get","post"]), name='products'),
    path('products/<int:pk>/', ProductsView.as_view(http_method_names=["get","post","delete"]), name='products with pk'),
    # ProductStocks API URLs
    path('productstocks/', ProductStocksView.as_view(http_method_names=["get","post"]), name='productstocks'),
    path('productstocks/<int:pk>/', ProductStocksView.as_view(http_method_names=["get","post","delete"]), name='productstocks with pk'),
    # DiscountVariations API URLs
    path('discountvariations/', DiscountVariationsView.as_view(http_method_names=["get","post"]), name='discountvariations'),
    path('discountvariations/<int:pk>/', DiscountVariationsView.as_view(http_method_names=["get","post","delete"]), name='discountvariations with pk'),
    # PriceVariations API URLs
    path('pricevariations/', PriceVariationsView.as_view(http_method_names=["get","post"]), name='pricevariations'),
    path('pricevariations/<int:pk>/', PriceVariationsView.as_view(http_method_names=["get","post","delete"]), name='pricevariations with pk'),
    # ProductColorsView API URLs
    path('productcolors/', ProductColorsView.as_view(http_method_names=["get","post"]), name='productcolors'),
    path('productcolors/<int:pk>/', ProductColorsView.as_view(http_method_names=["get","post","delete"]), name='productcolors with pk'),

    # All In One API URLs
    path("app-models-<str:appname>/",GetAppModels.as_view(),name="GetAppModels"),
    path("model-fields-<str:appname>-<str:modelname>/",GetModelFields.as_view(),name="GetModelFields"),
    path("all-in-one-<str:appname>-<str:modelname>/",AllInOne.as_view(),name="AllInOne"),
    path("all-in-one-<str:appname>-<str:modelname>/<int:pk>/",AllInOne.as_view(),name="AllInOne With PK"),
]

