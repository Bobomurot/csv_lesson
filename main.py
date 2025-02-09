
import csv
def get_country_column(file_name: str)-> list:
    """
    Bu funksiya fayl nomini qabul qiladi. Ushbu fayldan mamlakatlar(country) ning ro'yxatini chiqaring.
    Args:
        file_name: string
    Returns:
        list
    """
    f = open("data.csv", "r")
    read_csv = csv.reader(f)
    for line in read_csv:
        print(line[3])
a = get_country_column("data.csv")
print(a)