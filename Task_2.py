shopping_list = ["молоко", "хліб", "масло", "яйця", "сир", "яблука"]
long_names = [item for item in shopping_list if len(item) > 4]
print("Товари з назвою довше 4 символів:", long_names)
print("Кількість:", len(long_names))
