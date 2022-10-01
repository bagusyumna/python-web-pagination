class Pagination:
    def __init__(self, total_data, current_page, max_data_page):
        self.__total_data = total_data
        self.__current_page = current_page
        self.__max_data_page = max_data_page
        self.__check_init_params()

    def __check_init_params(self):
        if self.__max_data_page <= 0:
            self.__max_data_page = 100

        if self.__current_page <= 0:
            self.__current_page = 1
        elif self.__current_page > self.get_total_page():
            self.__current_page = self.get_total_page()

    def __create_pagination_obj(self):
        return {
            "limit": self.get_limit(),
            "offset": self.get_offset(),
            "current_page": self.__current_page,
            "total_page": self.get_total_page(),
            "page_number": self.get_pagination_page_number(),
        }

    def get_limit(self):
        return self.__max_data_page
    
    def get_offset(self):
        if self.__total_data <= 0:
            return 0
        return self.__max_data_page * (self.__current_page - 1)

    def get_total_page(self):
        mod_page = self.__total_data % self.__max_data_page
        return int(self.__total_data / self.__max_data_page) + (1 if mod_page < self.__max_data_page and mod_page > 0 else 0)

    def get_pagination_page_number(self):
        prev_page = (self.__current_page - 3 if self.__current_page >= 4 else 0) + 1
        next_page = (self.__current_page + 2 if self.__current_page <= self.get_total_page() - 3 else self.get_total_page()) + 1
        return list(range(prev_page, next_page))

    def get_pagination_dict(self):
        return dict(self.__create_pagination_obj())
