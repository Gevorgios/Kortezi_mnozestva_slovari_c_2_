# basketball_players = {}
#
# def add_player(name, height):
#     basketball_players[name] = height
#     print(f"{name} добавлен в базу данных")
#
# def remove_player(name):
#     if name in basketball_players:
#         del basketball_players[name]
#     else:
#         print(f"{name} не найден в базе данных")
#
# def search_player(name):
#     if name in basketball_players:
#         print(f"Имя: {name}, Рост: {basketball_players[name]}")
#     else:
#         print(f"{name} не найден в базе данных")
#
# def update_player(name, new_height):
#     if name in basketball_players:
#         basketball_players[name] = new_height
#         print(f"Информация о {name} обновлена")
#     else:
#         print(f"{name} не найден в базе данных")
#
# add_player("Michael Jordan", 198)
# add_player("LeBron James", 203)
#
# search_player("Michael Jordan")
# search_player("Kobe Bryant")
#
# update_player("LeBron James", 206)
# remove_player("Kobe Bryant")


# 2


# english_french_dict = {}
#
# def add_word(english_word, french_translation):
#     english_french_dict[english_word] = french_translation
#     print(f"Слово '{english_word}' с переводом '{french_translation}' добавлено в словарь")
#
# def remove_word(english_word):
#     if english_word in english_french_dict:
#         del english_french_dict[english_word]
#         print(f"Слово '{english_word}' удалено из словаря")
#     else:
#         print(f"Слово '{english_word}' не найдено в словаре")
#
# def search_word(english_word):
#     if english_word in english_french_dict:
#         print(f"Английское слово: {english_word}, Французский перевод {english_french_dict[english_word]}")
#     else:
#         print(f"Слово '{english_word}' не найдено в словаре")
#
# def update_word(english_word, new_french_translation):
#     if english_word in english_french_dict:
#         english_french_dict[english_word] = new_french_translation
#         print(f"Информация о слове '{english_word}' обновлена")
#     else:
#         print(f"Слово '{english_word}' не найдено в словаре")
#
# add_word("hello", "bonjour")
# add_word("apple", "pomme")
#
# search_word("hello")
# search_word("banana")
#
# update_word("apple", "pomme de terre")
# search_word("apple")
# remove_word("banana")



# 3

# company_info = {}
#
# def add_employee(name, phone, email, position, office_number, skype):
#     employee_info = {
#         "Phone": phone,
#         "Email": email,
#         "Position": position,
#         "Office Number": office_number,
#         "Skype": skype
#
#     }
#     company_info[name] = employee_info
#     print(f"{name} добавлен в базу данных")
#
# def remove_employee(name):
#     if name in company_info:
#         del company_info[name]
#         print(f"{name} удален из базы данных")
#
#     else:
#         print(f"{name} не найден в базе данных")
#
# def search_employee(name):
#     if name in company_info:
#         print(f"Информация о {name}: {company_info[name]}")
#     else:
#         print(f"{name} не найден в базе данных")
#
# def update_employee(name, field, new_value):
#     if name in company_info:
#         if field in company_info[name]:
#             company_info[name][field] = new_value
#             print(f"Информация о {name} обновлена")
#         else:
#             print(f"Информация о {name} обновлена")
#     else:
#         print(f"{name} не найден в базе данных")
#
# add_employee("John Doe", "1232323", "john@dasdsa", "Manager", "101", "john_skype")
# add_employee("Jane Smith", "987654321", "jane.smith@example.com", "Developer", "202", "jane_smith_skype")
#
# search_employee("John Doe")
# search_employee("Alice Brown")
# update_employee("Jane Smith", "Position", "Designer")
# remove_employee("Alice Brown")



# 4


# book_collection = {}
#
# def add_book(author, title, genre, year, pages, publisher):
#     book_info = {
#         "Author": author,
#         "Title": title,
#         "Genre": genre,
#         "Year": year,
#         "Pages": pages,
#         "Publsiher": publisher
#     }
#     book_collection[title] = book_info
#     print(f"Книга {title} добавлена в коллекцию")
#
# def remove_book(title):
#     if title in book_collection:
#         del book_collection[title]
#         print(f"Книга {title} удалена из коллекции")
#     else:
#         print(f"Книга {title} не найдена в коллекции")
#
# def search_book(title):
#     if title in book_collection:
#         print(f"Информация о книге {title}: {book_collection[title]}")
#     else:
#         print(f"Книга {title} не найдена в коллекции")
#
# def update_bok(title, field, new_value):
#     if title in book_collection:
#         if field in book_collection[title]:
#             book_collection[title][field] = new_value
#             print(f"Информация о книге {title} обновлена")
#         else:
#             print(f"Поле {field} не существует для книги {title}")
#     else:
#         print(f"Книга {title} не найдена в коллекции")
#
# add_book("Stephen King", "IT", "Horror", 1986, 1138, "Viking Press")
# add_book("J.K. Rowling", "Harry Potter and the Philosopher's Stone", "Fantasy", 1997, 223, "Bloomsbury")
#
# search_book("IT")
# search_book("The Great Gatsby")
#
# update_bok("Harry Potter and the Philosopher's Stone", "Year", 1998)
# remove_book("The Great Gatsby")

