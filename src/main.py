from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import TwoLineAvatarIconListItem, IRightBody
from kivymd.uix.button import MDIconButton


from utils import show_all_phones, phone_saver, show_all_for_name, show_all_for_phone
from models import User

class RightButton(IRightBody, MDIconButton):
    """ The only usefull part is IRightBody.
    Needed to align 'minus' icon button to the right
    in SearchResultItem 
    """
    pass
class SearchResultItem(TwoLineAvatarIconListItem):
    """Need to redefine ___init___ method in order to pass (stick) an extra param - user_id"""
    def __init__(self, user_id, **kwargs):
        super(SearchResultItem, self).__init__(**kwargs)
        self.user_id = user_id
    def delete_phone(self, user_id):
        if User.delete_by_id(user_id):
            self.parent.remove_widget(self)

class MainWindow(MDBoxLayout):
    pass

class PhoneBookApp(MDApp):

    def get_app_clear_search_list(self):
        app = MDApp.get_running_app()
        result_list_widget = app.root.ids.search_results
        result_list_widget.clear_widgets()
        return app, result_list_widget

    def show_all(self):
        _, result_list_widget = self.get_app_clear_search_list()
        for contact in show_all_phones():
            result_list_widget.add_widget(
                SearchResultItem(user_id=contact[2], text=f'ФИО: {contact[0]}', secondary_text=f' Тел: {contact[1]}')
            )
    def save_contact_and_switch_to_search(self, name, phones):
        if phone_saver(name, phones):
            app, _ = self.get_app_clear_search_list()
            sm = app.root.ids.bottom_nav
            sm.switch_tab('screen search')

    def name_search_and_populate_results_list(self, query):
        _, result_list_widget = self.get_app_clear_search_list()
        result_list_widget.clear_widgets()
        for contact in show_all_for_name(query):
            result_list_widget.add_widget(
                SearchResultItem(user_id=contact[2], text=f'ФИО: {contact[0]}', secondary_text=f' Тел: {contact[1]}')
            )
    def phone_search_and_populate_results_list(self, query):
        _, result_list_widget = self.get_app_clear_search_list()
        result_list_widget.clear_widgets()
        for contact in show_all_for_phone(query):
            result_list_widget.add_widget(
                SearchResultItem(user_id=contact[2], text=f'ФИО: {contact[0]}', secondary_text=f' Тел: {contact[1]}')
            )

    def build(self):
        self.title = 'Мега телефонная книга'
        self.theme_cls.primary_palette = "BlueGray"  # "Purple", "Red"
        self.icon = 'Mobile-icon.png'
        return MainWindow()

if __name__ == '__main__':
    PhoneBookApp().run()