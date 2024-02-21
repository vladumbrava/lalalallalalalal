from domain.sale import Sale

class SaleRepository:
    def __init__(self)
        self.__sales = []

    def get_sales(self):
        return self.__sales

    def set_sales(self, sales):
        self.__sales = sales

    def add_sale(self, sale):
        if not isinstance(sale, Sale):
            raise ValueError("error")
        self.__sales.append(sale)

    def get_sales_of_category(self, category):
        result = ""
        for sal in self.__sales:
            if sal.get_category() == category:
                result += f"{sal}\n"
        return result

    def __str__(self):
        result = ""
        for sal in self.__sales:
            result += f"{sal}\n"
        return result