from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CatalogViewSetPagination(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 200

    def get_paginated_response(self, data):
        return Response({
            'results': data,
            'currentPage': self.page.number,
            'lastPage': self.page.paginator.num_pages
        })
