from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, os



f = open('./app/brands.json')
data = json.load(f)

def paginate(data, page, limit):
    start = (page - 1) * limit
    end = start + limit
    return data[start:end]



class BrandListView(APIView):

    def get(self, request):
        category = self.request.query_params.get('category')
        page = int(self.request.query_params.get('page', 1))
        limit = int(self.request.query_params.get('limit', 10))
        filtered_data = []
        brands = data
        if category:
            for brand in data:
                tags = brand['tags'].split(',')
                if category in tags:
                    filtered_data.append(brand)
                    brands = filtered_data
        return Response(paginate(brands,page,limit), status=status.HTTP_200_OK)

class TagsListView(APIView):

    def get(self, request):
        tags = []
        for brand in data:
            tags.extend(brand['tags'].split(','))
        return Response(list(set(tags)), status=status.HTTP_200_OK)
        
