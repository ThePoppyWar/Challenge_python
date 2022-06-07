class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author =author
        if self.check_isbn(isbn) == False:
            raise ValueError("Wrong ISBN")
        else:
            self.isbn = isbn


    @staticmethod
    def check_isbn(isbn: str):
        isbn = isbn.replace("-", "").replace(" ", "")
        check_number = int(isbn[-1])
        if not isbn.isdigit():
            return False
        if len(isbn) == 10:
            result = 0
            for i, number in enumerate(isbn):
                result += (i + 1) * int(number)
                if (result % 11) == check_number:
                    return True
                else:
                    return False
        if len(isbn) == 13:
            result_13 = 0
            for i, number in enumerate(isbn):
                if i % 2 == 0:
                    result_13 += int(number) * 1
                if i % 2 != 0:
                    result_13 += int(number) * 3
                    if (result_13 % 10) == 0 and (result_13 % 10) == check_number:
                        return True
                    else:
                        return False
                if 10 - (result_13 % 10) == check_number:
                    return True

            else:
                return False
        else:
            return False

print(Book.check_isbn('978139316093'))
print(Book.check_isbn("978-3-16-148410-0"))
print(Book.check_isbn("978-83-7181-510-2"))