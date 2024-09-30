import requests
from bs4 import BeautifulSoup


# Функция для получения ссылки на статью по запросу
def search_wikipedia(query):
    url = f"https://ru.wikipedia.org/wiki/{query.replace(' ', '_')}"
    return url


# Функция для получения и парсинга страницы
def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем наличие ошибок HTTP
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")
        return None


# Функция для вывода первых нескольких параграфов статьи
def print_paragraphs(soup, num_paragraphs=3):
    paragraphs = soup.find_all('p')
    for i, p in enumerate(paragraphs[:num_paragraphs], start=1):
        print(f"Параграф {i}: {p.text.strip()}")
        print()


# Функция для получения ссылок на связанные статьи
def get_related_links(soup):
    links = soup.find_all('a', href=True)
    related_links = {}
    for link in links:
        if link['href'].startswith('/wiki/') and ':' not in link['href']:  # Пропускаем технические и служебные статьи
            related_links[link.text] = f"https://ru.wikipedia.org{link['href']}"
    return related_links


# Главная функция игры
def wikipedia_game():
    print("Добро пожаловать в Википедию через консоль!")

    # Получаем первый запрос от пользователя
    initial_query = input("Введите запрос для поиска: ")
    url = search_wikipedia(initial_query)

    while True:
        # Загружаем страницу
        soup = get_page_content(url)
        if soup is None:
            print("Не удалось загрузить страницу. Попробуйте другой запрос.")
            break

        print("\nТекущая статья:", soup.find('h1').text)  # Заголовок статьи
        print_paragraphs(soup)

        # Получаем список связанных страниц
        related_links = get_related_links(soup)

        # Предлагаем действия пользователю
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        user_choice = input("Введите номер действия (1, 2, 3): ")

        if user_choice == '1':
            print("Вы листаете параграфы текущей статьи.")
            print_paragraphs(soup, num_paragraphs=5)

        elif user_choice == '2':
            if related_links:
                print("\nСвязанные статьи:")
                for i, (link_text, link_url) in enumerate(related_links.items(), start=1):
                    print(f"{i}. {link_text}")

                link_choice = input("Введите номер ссылки для перехода или 'q' для возврата: ")
                if link_choice.isdigit() and 1 <= int(link_choice) <= len(related_links):
                    selected_link = list(related_links.values())[int(link_choice) - 1]
                    url = selected_link
                else:
                    print("Неверный выбор. Возвращаемся к текущей статье.")
            else:
                print("Нет связанных статей.")

        elif user_choice == '3':
            print("Спасибо за использование программы!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    wikipedia_game()
