import flet as ft
import googletrans
from forecast import weather_forecast

def main(page):
    page.title = "Weather App"
    # Установка темы для приложения
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.BLUE_900, secondary=ft.colors.BLUE_700))

    # Создание текстового поля с улучшенным стилем
    city = ft.TextField(label="City", autofocus=True, border_radius=20, filled=True, prefix_icon=ft.icons.PLACE)

    # Колонка для приветствия и результатов
    greetings = ft.Column()

    # Приветственное сообщение
    greetings.controls.append((ft.Text('Welcome!')))

    def btn_go(e):
        try:
            if city.value:
                temp, weather = weather_forecast(city.value)
                temp = round(temp, 1)
                weather_translated = googletrans.Translator().translate(weather, dest='ukrainian').text
                # Очистка предыдущих сообщений
                greetings.controls.clear()
                # Отображение результата в красивом формате
                result_text = ft.Text(f"Температура: {temp}°C, {weather_translated}")
                greetings.controls.append(result_text)
        except Exception as ex:
            greetings.controls.clear()
            greetings.controls.append(ft.Text("Ошибка: Невозможно найти указанный город. Пожалуйста, проверьте написание.", style=ft.TextStyle(color=ft.colors.RED_700)))
        finally:
            page.update()
            city.value = ""

    # Кнопка с улучшенным стилем
    go_button = ft.ElevatedButton('Let\'s go!', on_click=btn_go, icon=ft.icons.SEARCH, style=ft.ButtonStyle(elevation=10))

    # Добавление элементов на страницу
    page.add(ft.Row([city, go_button], alignment="center"))
    page.add(greetings)

ft.app(target=main)
