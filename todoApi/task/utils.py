from django.core.paginator import Paginator, InvalidPage, PageNotAnInteger, EmptyPage

def get_paginator(request, qs):
    try:
        page = int(request.query_params.get("page", 0))
        limit = int(request.query_params.get("limit", 10))

    except ValueError:
        page, limit = 1, 10

    paginator = Paginator(qs, limit)

    try:
        page_object = paginator.page(page)
        object_list = page_object.object_list

    except (InvalidPage, PageNotAnInteger, EmptyPage):
        return qs, paginator.count, None

    return object_list, paginator.count, page
