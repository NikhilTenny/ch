class ModelPagination:

    def __init__(self):
        self.paginate_params = {}

    def create_pagination_params(self, request_data):
        self.paginate_params = {
            "per_page": request_data.get("per_page", 10),
            "offset": request_data.get("offset", 0),
            "order": request_data.get("order", "ASC"),
            "order_by": request_data.get("order_by", "id")
        }

    def paginate_queryset(self, queryset):
        """
            Paginate a queryset based on provided pagination parameters.
        """
        per_page = int(self.paginate_params["per_page"])
        offset = int(self.paginate_params["offset"])
        order = self.paginate_params["order"]
        order_by = self.paginate_params["order_by"]
        if order == "ASC":
            base_queryset = queryset.order_by("id")
        else:
            base_queryset = queryset.order_by(f"-{order_by}")

        result_queryset = base_queryset[offset:offset + per_page]
        return result_queryset
