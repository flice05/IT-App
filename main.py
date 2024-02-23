from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file("my.kv")


class MainWindow(Screen):
    def eight_button_on_press(self):
        self.manager.current = "eight"

    def nine_button_on_press(self):
        self.manager.current = "nine"

    def ten_button_on_press(self):
        self.manager.current = "ten"


class EightGrade(Screen):
    def back_to_main_window(self):
        self.manager.current = "main"


class NineGrade(Screen):
    def back_to_main_window(self):
        self.manager.current = "main"


class TenGrade(Screen):
    def back_to_main_window(self):
        self.manager.current = "main"


class EightTasks(Screen):
    pass


class NineTasks(Screen):
    pass


class TenTasks(Screen):
    pass

class MyApp(App):

    def build(self):

        screen_manager = ScreenManager()
        screen_manager.add_widget(MainWindow(name="main"))
        screen_manager.add_widget(EightGrade(name="eight"))
        screen_manager.add_widget(NineGrade(name="nine"))
        screen_manager.add_widget(TenGrade(name="ten"))

        screen_manager.current = "main"

        return screen_manager


if __name__ == "__main__":
    MyApp().run()
