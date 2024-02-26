import pyodbc
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


Builder.load_file("my.kv")


class MainWindow(Screen):
    pass


class EightGrade(Screen):
    "Окно с типами заданий для 8 класса"
    def show_eight_tasks(self, instance):
        task_type = instance.text
        nine_task_window = EightTaskWindow(task_type=task_type)
        self.manager.add_widget(nine_task_window)
        self.manager.current = "eight_task"


class EightTaskWindow(Screen):
    "Окно с заданиями конкретного типа для 8 класса"
    def __init__(self, task_type, **kwargs):
        super(EightTaskWindow, self).__init__(**kwargs)
        ###################################################################################################################
        ###################################################################################################################
        ###################################################################################################################
        ###################################################################################################################


class NineGrade(Screen):
    "Окно с типами заданий для 9 класса"
    def show_nine_tasks(self, instance):
        task_type = instance.text
        nine_task_window = NineTaskWindow(task_type=task_type)
        self.manager.add_widget(nine_task_window)
        self.manager.current = "nine_task"


class NineTaskWindow(Screen):
    "Окно с заданиями конкретного типа для 9 класса"
    def __init__(self, task_type, **kwargs):
        super(NineTaskWindow, self).__init__(**kwargs)
        ###################################################################################################################
        ###################################################################################################################
        ###################################################################################################################
        ###################################################################################################################


class TenGrade(Screen):
    "Окно с типами заданий для 10 класса"
    def show_ten_tasks(self, instance):
        task_type = instance.text
        ten_task_window = TenTaskWindow(task_type=task_type)
        self.manager.add_widget(ten_task_window)
        self.manager.current = "ten_task"


class TenTaskWindow(Screen):
    "Окно с заданиями конкретного типа для 10 класса"
    def __init__(self, task_type, **kwargs):
        super(TenTaskWindow, self).__init__(**kwargs)
        ###################################################################################################################
        ###################################################################################################################
        ###################################################################################################################
        ###################################################################################################################


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainWindow(name="main"))
        screen_manager.add_widget(EightGrade(name="eight"))
        screen_manager.add_widget(NineGrade(name="nine"))
        screen_manager.add_widget(TenGrade(name="ten"))
        screen_manager.add_widget(EightTaskWindow(name="eight_task", task_type=None))
        screen_manager.add_widget(NineTaskWindow(name="nine_task", task_type=None))
        screen_manager.add_widget(TenTaskWindow(name="ten_task", task_type=None))
        screen_manager.current = "main"
        return screen_manager


if __name__ == "__main__":
    MyApp().run()
