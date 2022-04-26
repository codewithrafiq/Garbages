from traceback import print_tb
from unicodedata import category
from rest_framework import permissions, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import *
from django.apps import apps
from enumfields import EnumField
from products.helper import generate_category


class GetAppModels(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
        authentication.BasicAuthentication, ]

    def get(self, request, appname, *args, **kwargs):
        """ Give me any app name I will Give you all models name """
        return Response(str([d.__name__ for d in dict(apps.all_models[appname]).values()]))


class GetModelFields(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
        authentication.BasicAuthentication, ]

    def get(self, request, appname, modelname, *args, **kwargs):
        """ 
        Give me any app and model name I will Give you all fields Details 
        """
        result = []
        modeltype = apps.get_model(app_label=appname, model_name=modelname)
        print(modeltype._meta)
        fields = modeltype._meta.fields
        try:
            for field in fields:
                res = {}
                res["field_name"] = str(field).split('.')[2]
                res["datatype"] = str(field.__class__).split(
                    '.')[-1].replace('\'>', '')
                res["is_null"] = field.null
                if field.__class__ is EnumField:
                    res["choices"] = ["{}:{}".format(choice[1], str(
                        choice[-1])) for choice in field.choices]
                result.append(res)
            return Response(result)
        except Exception as e:
            return Response(str(e))


class AllInOne(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [authentication.TokenAuthentication,
                              authentication.SessionAuthentication,
                              authentication.BasicAuthentication, ]

    def get(self, request, appname, modelname, pk=None, *args, **kwargs):
        modeltype = apps.get_model(app_label=appname, model_name=modelname)
        modelName = str(str(modeltype._meta).split('.')[1]).capitalize()
        serializerName = modelName + 'Serializer'
        serializer = eval(serializerName)
        if pk:
            todo_objs = modeltype.objects.filter(pk=pk).first()
            serializer_instance = serializer(todo_objs)
            return Response(serializer_instance.data)
        todo_objs = modeltype.objects.all()
        print("todo_objs--------->", todo_objs)
        serializer_instance = serializer(todo_objs, many=True)
        return Response(serializer_instance.data)

    def post(self, request, appname, modelname, pk=None, *args, **kwargs):
        modeltype = apps.get_model(app_label=appname, model_name=modelname)
        modelName = str(str(modeltype._meta).split('.')[1]).capitalize()
        serializerName = modelName + 'Serializer'
        serializer = eval(serializerName)
        if pk:
            todo_objs = modeltype.objects.filter(pk=pk).first()
            serializer_instance = serializer(todo_objs, data=request.data)
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(serializer_instance.data)
            else:
                return Response(serializer_instance.errors)
        else:
            serializer_instance = serializer(data=request.data)
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(serializer_instance.data)
            else:
                return Response(serializer_instance.errors)

    def delete(self, request, appname, modelname, pk=None, *args, **kwargs):
        if pk:
            modeltype = apps.get_model(app_label=appname, model_name=modelname)
            todo_objs = modeltype.objects.filter(pk=pk).first()
            todo_objs.delete()
            return Response("Deleted")
        else:
            return Response("Please provide pk")


class ColorView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

    def get(self, request, pk=None):
        try:
            if pk:
                color_obj = Color.objects.get(pk=pk)
                serializer = ColorSerializer(color_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            color_obj = Color.objects.all()
            serializer = ColorSerializer(color_obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk=None):
        try:
            if pk:
                color_obj = Color.objects.get(pk=pk)
                serializer = ColorSerializer(color_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer = ColorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            color_obj = Color.objects.get(pk=pk)
            color_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BrandView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

    def get(self, request, pk=None):
        try:
            if pk:
                brand_obj = Brand.objects.get(pk=pk)
                serializer = BrandSerializer(brand_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            brand_obj = Brand.objects.all()
            serializer = BrandSerializer(brand_obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk=None):
        try:
            if pk:
                brand_obj = Brand.objects.get(pk=pk)
                serializer = BrandSerializer(brand_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer = BrandSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            brand_obj = Brand.objects.get(pk=pk)
            brand_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UnitesView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

    def get(self, request, pk=None):
        try:
            if pk:
                unite_obj = Unites.objects.get(pk=pk)
                serializer = UnitesSerializer(unite_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            unite_obj = Unites.objects.all()
            serializer = UnitesSerializer(unite_obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk=None):
        try:
            if pk:
                unite_obj = Unites.objects.get(pk=pk)
                serializer = UnitesSerializer(unite_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer = UnitesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            unite_obj = Unites.objects.get(pk=pk)
            unite_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CurrenciesView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

    def get(self, request, pk=None):
        try:
            if pk:
                currency_obj = Currencies.objects.get(pk=pk)
                serializer = CurrenciesSerializer(currency_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            currency_obj = Currencies.objects.all()
            serializer = CurrenciesSerializer(currency_obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk=None):
        try:
            if pk:
                currency_obj = Currencies.objects.get(pk=pk)
                serializer = CurrenciesSerializer(
                    currency_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer = CurrenciesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            currency_obj = Currencies.objects.get(pk=pk)
            currency_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CategoriesView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication,]

    def get(self, request, pk=None):
        categorys = Categorie.objects.all()
        """data = []
        for category in categorys:
            single_category = CategoriesSerializer(category).data
            single_category["sub_categorie"] = CategoriesSerializer(Categorie.objects.filter(sub_categorie__id=category.id), many=True).data
            data.append(single_category)"""
        categories = []
        cat_res = []
        for cat in categorys:
            cat_obj = {}
            cat_obj["id"] = cat.id
            cat_obj["fk"] = cat.sub_categorie
            cat_obj["name"] = cat.name
            cat_obj["deescription"] = cat.deescription
            if not cat_obj["fk"]:
                cat_obj["fk"] = "null"
            else:
                cat_obj["fk"] = cat_obj["fk"].id
            categories.append(cat_obj)
        data = generate_category(0, categories,cat_res)

        return Response(data, status=status.HTTP_200_OK)

    # def get(self, request, pk=None):
    #     try:
    #         if pk:
    #             category_obj = Categorie.objects.get(pk=pk)
    #             serializer = CategoriesSerializer(category_obj)
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         category_obj = Categorie.objects.all()
    #         serializer = CategoriesSerializer(category_obj, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk=None):
        try:
            if pk:
                category_obj = Categorie.objects.get(pk=pk)
                serializer = CategoriesSerializer(
                    category_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer = CategoriesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
        print("CategoriesView-------------",request.data)
        try:
            cat_serilizer = CategoriesSerializer(data={'name':request.data['name'],'sub_categorie':request.data['hcat_id']})
            if cat_serilizer.is_valid():
                cat_serilizer.save()
                return Response(cat_serilizer.data, status=status.HTTP_200_OK)
            return Response(cat_serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            category_obj = Categorie.objects.get(pk=pk)
            category_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProductsView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

    def get(self, request, pk=None):
        try:
            if pk:
                product_obj = Product.objects.get(pk=pk)
                serializer = ProductSerializer(product_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            product_obj = Product.objects.all()
            serializer = ProductSerializer(product_obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk=None):
        try:
            if pk:
                product_obj = Product.objects.get(pk=pk)
                serializer = ProductSerializer(product_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product_obj = Product.objects.get(pk=pk)
            product_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProductStocksView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

    def get(self, request, pk=None):
        try:
            if pk:
                product_stock_obj = ProductStocks.objects.get(pk=pk)
                serializer = ProductStocksSerializer(product_stock_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            product_stock_obj = ProductStocks.objects.all()
            serializer = ProductStocksSerializer(product_stock_obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk=None):
        try:
            if pk:
                product_stock_obj = ProductStocks.objects.get(pk=pk)
                serializer = ProductStocksSerializer(
                    product_stock_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer = ProductStocksSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product_stock_obj = ProductStocks.objects.get(pk=pk)
            product_stock_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DiscountVariationsView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

    def get(self, request, pk=None):
        try:
            if pk:
                discount_variation_obj = DiscountVariations.objects.get(pk=pk)
                serializer = DiscountVariationsSerializer(
                    discount_variation_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            discount_variation_obj = DiscountVariations.objects.all()
            serializer = DiscountVariationsSerializer(
                discount_variation_obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk=None):
        try:
            if pk:
                discount_variation_obj = DiscountVariations.objects.get(pk=pk)
                serializer = DiscountVariationsSerializer(
                    discount_variation_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer = DiscountVariationsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            discount_variation_obj = DiscountVariations.objects.get(pk=pk)
            discount_variation_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PriceVariationsView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

    def get(self, request, pk=None):
        try:
            if pk:
                price_variation_obj = PriceVariations.objects.get(pk=pk)
                serializer = PriceVariationsSerializer(price_variation_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            price_variation_obj = PriceVariations.objects.all()
            serializer = PriceVariationsSerializer(
                price_variation_obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk=None):
        try:
            if pk:
                price_variation_obj = PriceVariations.objects.get(pk=pk)
                serializer = PriceVariationsSerializer(
                    price_variation_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer = PriceVariationsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            price_variation_obj = PriceVariations.objects.get(pk=pk)
            price_variation_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProductColorsView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

    def get(self, request, pk=None):
        try:
            if pk:
                product_color_obj = ProductColors.objects.get(pk=pk)
                serializer = ProductColorsSerializer(product_color_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            product_color_obj = ProductColors.objects.all()
            serializer = ProductColorsSerializer(product_color_obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk=None):
        try:
            if pk:
                product_color_obj = ProductColors.objects.get(pk=pk)
                serializer = ProductColorsSerializer(
                    product_color_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer = ProductColorsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product_color_obj = ProductColors.objects.get(pk=pk)
            product_color_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
