from user import User
import crypt

from functools import partial
import math

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.core.clipboard import Clipboard
from kivy.uix.checkbox import CheckBox
from kivy.graphics import Color, Line
from kivy.config import Config

class MainApp(App):

    def checkbox_default_server_click(self, checkbox):
        if self.checkbox_default_server.active:
            self.b1_input.text = 'default.todo'
            self.b1_input.disabled = True
            self.b2_input.text = '3306'
            self.b2_input.disabled = True

            self.b1_input.background_color = (.564, .729, 1, 1)
            self.b1_input.foreground_color = (0, 0, 0, 1)
            self.b2_input.background_color = (.564, .729, 1, 1)
            self.b2_input.foreground_color = (0, 0, 0, 1)
        else:
            self.b1_input.text = ''
            self.b1_input.disabled = False
            self.b2_input.text = ''
            self.b2_input.disabled = False

            self.b1_input.foreground_color = (1, 1, 1, 1)
            self.b1_input.background_color = (0, 0, 0, 0)
            self.b2_input.background_color = (0, 0, 0, 0)
            self.b2_input.foreground_color = (1, 1, 1, 1)

    def add_element(self, widget):
            self.hide_elements()

            #####################################    
            ### -------- Add element -------- ###
            #####################################
            self.add_element_main_layout = BoxLayout(orientation='vertical')
            self.add_element_layout = BoxLayout(orientation='vertical', size_hint=(1, .7))

            self.add_element_b1_label = LeftAlignedLabel(
                                                text='WEBSITE',
                                                pos_hint={'center_x': .5, 'center_y': .5})
            self.add_element_b1_input = RoundedTextInput(
                                                size_hint=(.95, None),
                                                height='40dp',
                                                padding='8dp',
                                                pos_hint={'center_x': .5, 'center_y': .5})
            self.add_element_b2_label = LeftAlignedLabel(
                                                text='LOGIN',
                                                pos_hint={'center_x': .5, 'center_y': .5})
            self.add_element_b2_input = RoundedTextInput(
                                                size_hint=(.95, None),
                                                height='40dp',
                                                padding='8dp',
                                                pos_hint={'center_x': .5, 'center_y': .5})
            self.add_element_b3_label = LeftAlignedLabel(
                                                text='PASSWORD', 
                                                pos_hint={'center_x': .5, 'center_y': .5})
            self.add_element_b3_input = RoundedTextInput(
                                                size_hint=(.95, None),
                                                height='40dp',
                                                padding='8dp',
                                                pos_hint={'center_x': .5, 'center_y': .5})
            self.add_element_b4_label = LeftAlignedLabel(
                                                text='CHOOSE IMAGE', 
                                                pos_hint={'center_x': .5, 'center_y': .5})
            self.add_element_scroll_list = ScrollView(do_scroll_y=True, size_hint=(1, .6))
            self.add_element_list = GridLayout(
                                                cols=4, 
                                                size_hint=(1, None),
                                                spacing='5dp')

            self.add_element_list_image = dict()
            i = 0
            for f in self.website_images:
                self.add_element_list_image[i] = Button(
                                background_normal=f'./img/websites/{f}',
                                border=(0,0,0,0),
                                size_hint=(1, 1))

                self.add_element_list_image[i].bind(on_press=partial(self.choose_image, i))
                self.add_element_list.add_widget(self.add_element_list_image[i])
                i+=1
                
            self.add_element_list.height = f'{str(90*math.ceil(i / 4))}dp'
            self.add_element_scroll_list.add_widget(self.add_element_list)

            self.add_element_button = RoundedButton(
                                text='ADD ELEMENT',
                                size_hint=(.95, None),
                                height='50dp',
                                font_size='25dp',
                                bold=True,
                                pos_hint={"center_x": .5, "center_y": 1})
            self.add_element_button.bind(on_press = self.insert_element)
            self.choosen_image = ''
            
            self.add_element_margin1 = Label(text='', size_hint=(.1, .1))
            self.add_element_margin2 = Label(text='', size_hint=(.1, .3))
            self.add_element_margin3 = Label(text='', size_hint=(.1, .05))

            self.add_element_layout.add_widget(self.add_element_b1_label)
            self.add_element_layout.add_widget(self.add_element_b1_input)
            self.add_element_layout.add_widget(self.add_element_b2_label)
            self.add_element_layout.add_widget(self.add_element_b2_input)
            self.add_element_layout.add_widget(self.add_element_b3_label)
            self.add_element_layout.add_widget(self.add_element_b3_input)

            self.add_element_layout.add_widget(self.add_element_b4_label)
            self.add_element_layout.add_widget(self.add_element_scroll_list)

            self.add_element_layout.add_widget(self.add_element_margin3)
            self.add_element_layout.add_widget(self.add_element_button)

            self.add_element_main_layout.add_widget(self.add_element_margin1)
            self.add_element_main_layout.add_widget(self.add_element_layout)
            self.add_element_main_layout.add_widget(self.add_element_margin2)
            self.main_layout.add_widget(self.add_element_main_layout)

    def choose_image(self, i, widget):
        for j, x in enumerate(range(30)):
            try: self.add_element_list_image[j].background_color = (1, 1, 1, 1)
            except: pass

        self.add_element_list_image[i].background_color = (1, 1, 1, .2)
        self.choosen_image = self.add_element_list_image[i].background_normal.split(f'/')[-1]

    def insert_element(self, widget):
        self.u.insert(self.add_element_b1_input.text, self.add_element_b2_input.text, self.add_element_b3_input.text, self.choosen_image)
        self.main_layout.remove_widget(self.add_element_main_layout)
        self.show_elements()

    def clipboard_element(self, element, widget):
        Clipboard.copy(element.text)

    def decrypt_element(self, n, widget):
        try: self.label_password[n].text = crypt.decrypt(self.passwords[n][3], self.u.key)
        except: pass
        self.label_password[n].do_cursor_movement(action='cursor_home', control=False, alt=False)

    def delete_element(self, p, widget):
        self.hide_elements()

        ########################################   
        ### -------- Delete element -------- ###
        ########################################
        self.delete_element_main_layout = BoxLayout(orientation='vertical', padding='30dp')
        self.delete_element_label = Label(
                                text=f'Do you want to delete "{p[1]}" ?', 
                                size_hint=(1, .2), 
                                font_size='20dp',
                                bold=True,
                                pos_hint={"center_x": .5, "center_y": .5})
        self.delete_element_buttons = BoxLayout(
                                orientation='horizontal', 
                                size_hint=(1, .05))

        self.delete_element_button_yes = RoundedButtonDelete(
                                text='Delete',
                                size_hint=(.45, None),
                                height='50dp',
                                font_size='25dp',
                                bold=True,
                                pos_hint={"center_x": .5, "center_y": .5})
        self.delete_element_button_no = RoundedButton(
                                text='Cancel',
                                size_hint=(.45, None),
                                height='50dp',
                                font_size='25dp',
                                bold=True,
                                pos_hint={"center_x": .5, "center_y": .5})

        self.delete_element_button_yes.bind(on_press=partial(self.drop_element, p[0], True))
        self.delete_element_button_no.bind(on_press=partial(self.drop_element, p[0], False))

        self.delete_element_margin1 = Label(size_hint=(1, .35))
        self.delete_element_margin2 = Label(size_hint=(1, .55))
        self.delete_element_margin3 = Label(size_hint=(.1, 1))

        self.delete_element_buttons.add_widget(self.delete_element_button_yes)
        self.delete_element_buttons.add_widget(self.delete_element_margin3)
        self.delete_element_buttons.add_widget(self.delete_element_button_no)

        self.delete_element_main_layout.add_widget(self.delete_element_margin1)
        self.delete_element_main_layout.add_widget(self.delete_element_label)
        self.delete_element_main_layout.add_widget(self.delete_element_buttons)
        self.delete_element_main_layout.add_widget(self.delete_element_margin2)

        self.main_layout.add_widget(self.delete_element_main_layout)

    def drop_element(self, n, drop, widget):
        if drop: self.u.delete(n)
        self.main_layout.remove_widget(self.delete_element_main_layout)
        self.show_elements(searched=self.searched_text)
            
    def search_element(self, widget, element):
        if self.searched_text != self.search_element_input.text:
            self.searched_text = self.search_element_input.text
            self.hide_elements()
            self.show_elements(searched=self.search_element_input.text)
            self.search_element_input.focus = True
    
    def show_elements(self, searched=''):
        #############################
        ### -------- App -------- ###
        #############################
        self.passwords = self.u.get()
       
        self.visible_elements = 0
        for p in self.passwords:
            if searched in p[1]:
                self.visible_elements += 1

        self.scroll_layout = ScrollView(do_scroll_y=True)
        self.app_layout = BoxLayout(orientation='vertical', size_hint=(1, None), height=f'{self.visible_elements*115+55}dp', spacing='15dp')
        self.menu = BoxLayout(orientation='horizontal', spacing='10dp', height='55dp')

        self.app_layout.add_widget(self.menu)
        self.scroll_layout.add_widget(self.app_layout)
        self.main_layout.add_widget(self.scroll_layout)
        
        self.add_element_button = RoundedButton(
                            text='ADD ELEMENT',
                            size_hint=(.5, None),
                            height='55dp',
                            font_size='25dp',
                            bold=True)
        self.add_element_button.bind(on_press = self.add_element)

        self.search_element_input = SearchInput()
        self.search_element_input.bind(text=self.search_element)
        self.search_element_input.text = searched

        self.menu.add_widget(self.add_element_button)
        self.menu.add_widget(self.search_element_input)

        # Dictionaries for subboxes
        self.border_main_subbox = dict()

        self.title_main_subbox = dict()
        self.main_subbox = dict()

        self.logo_subbox = dict()
        self.grid_subbox = dict()

        self.label_login = dict()
        self.button_login_copy = dict()
        self.button_delete = dict()
        self.label_password = dict()
        self.button_password_copy = dict()
        self.button_decrypt = dict()

        # Subbox
        for i, p in enumerate(self.passwords):
            if searched in p[1]:
                self.border_main_subbox[i] = BoxLayout(orientation='vertical', size_hint=(1, None), height='100dp')
                self.title_main_subbox[i] = ElementTitle(text=p[1])
                self.main_subbox[i] = BoxLayout(orientation='horizontal', size_hint=(1, None), height='75dp')
               
                # Image
                self.logo_subbox[i] = Image(
                                size_hint=(.2, 1), 
                                pos_hint={'center_x': .5, 'center_y': .5})
                self.logo_subbox[i].source=f'./img/websites/{p[4]}' if p[4] != '' else './img/shield.png'

                self.grid_subbox[i] = GridLayout(cols=3, size_hint=(.8, 1), spacing='3dp')

                # Grid row1
                self.label_login[i] = ElementTextInput(
                                text=crypt.decrypt(p[2], self.u.key),
                                size_hint=(.75, .5),
                                multiline=False,
                                readonly=True,
                                font_size='16dp',
                                padding='7dp')
                self.button_login_copy[i] = Button(
                                background_color=(.564, .729, 1, 1),
                                background_normal='',
                                text='copy',
                                size_hint=(.15, .1),
                                font_size='18dp',
                                bold=True)
                self.button_delete[i] = DeleteButton(
                                text='',
                                size_hint=(.1, .1),
                                font_size='20dp',
                                bold=True,
                                background_normal='',
                                background_color=(1,0,0,1))

                # Grid row2
                self.label_password[i] = ElementTextInput(
                                text=f'{p[3][0:15]}...',
                                size_hint=(.75, .5),
                                multiline=False,
                                readonly=True,
                                font_size='16dp',
                                padding='7dp')
                self.button_password_copy[i] = Button(
                                background_color=(.564, .729, 1, 1),
                                background_normal='',
                                text='copy',
                                size_hint=(.15, .1),
                                font_size='18dp',
                                bold=True)
                self.button_decrypt[i] = Button(
                                background_color=(.564, .729, 1, 1),
                                color=(0,0,1,1),
                                background_normal='',
                                text='D',
                                size_hint=(.1, .1),
                                font_size='20dp',
                                bold=True)

                # Buttons' on_press
                self.button_login_copy[i].bind(on_press = partial(self.clipboard_element, self.label_login[i]))
                self.button_password_copy[i].bind(on_press = partial(self.clipboard_element, self.label_password[i]))
                self.button_delete[i].bind(on_press = partial(self.delete_element, p))
                self.button_decrypt[i].bind(on_press = partial(self.decrypt_element, i))

                # Create subbox
                self.app_layout.add_widget(self.border_main_subbox[i])

                self.border_main_subbox[i].add_widget(self.title_main_subbox[i])
                self.border_main_subbox[i].add_widget(self.main_subbox[i])

                self.main_subbox[i].add_widget(self.logo_subbox[i])
                self.main_subbox[i].add_widget(self.grid_subbox[i])

                self.grid_subbox[i].add_widget(self.label_login[i])
                self.grid_subbox[i].add_widget(self.button_login_copy[i])
                self.grid_subbox[i].add_widget(self.button_delete[i])
                self.grid_subbox[i].add_widget(self.label_password[i])
                self.grid_subbox[i].add_widget(self.button_password_copy[i])
                self.grid_subbox[i].add_widget(self.button_decrypt[i])

    def hide_elements(self):
        self.main_layout.remove_widget(self.scroll_layout)
        self.scroll_layout = None

    def login(self, widget):
        try:
            self.u = User(self.b1_input.text, self.b2_input.text, self.b3_input.text, self.b4_input.text, self.b5_input.text)
            self.u.get(decrypt=True)
        except:
            self.info_label.color = (1,0,0,1)
            self.info_label.text = 'Login failed!'
        else:
            self.info_label.color = (0,1,0,1)
            self.info_label.text = 'Logged in successfuly!'
            self.login_layout.opacity = 0
            self.login_layout.size_hint = (0,0)

            self.show_elements()
            self.searched_text = ''

    def build(self):
        # START
        self.title = 'mysqlvault'
        self.icon = './img/password.png'
        Config.set('kivy', 'window_icon', './img/password.png')
        self.website_images = ['4chan.png', 'aliexpress.png', 'amazon.png', 'apple.png', 'ebay.png', 'facebook.png', 'google.png', 'instagram.png', 'mega.png', 'microsoft.png', 'netflix.png', 'paypal.png', 'reddit.png', 'snapchat.png', 'steam.png', 'tiktok.png', 'twitch.png', 'twitter.png', 'whatsup.png', 'youtube.png']
        self.main_layout = BoxLayout(orientation='vertical', padding='10dp')
        Window.size = (421, 912)

        #########################
        ### ----- Login ----- ###
        #########################
        self.login_layout = BoxLayout(orientation='vertical', spacing='5dp')
        self.main_label = Label(
                            text='mysqlvault',
                            size_hint=(.65, .25),
                            font_size='33dp',
                            bold=True,
                            pos_hint={'center_x': .5, 'center_y': 1})
        self.logo = Image(
                            source='./img/password.png', 
                            size_hint=(.3, .3), 
                            pos_hint={'center_x': .5, 'center_y': 1})
        self.info_label = Label(
                            text='',
                            size_hint=(.5, .05),
                            font_size='20dp',
                            pos_hint={'center_x': .5, 'center_y': 1})

        self.checkbox_default_server_layout = BoxLayout(orientation='horizontal', spacing='5dp', size_hint=(1, .1))
        self.checkbox_default_server_label = RightAlignedLabel(
                                    text='USE DEFAULT',
                                    size_hint=(.9, 1),
                                    font_size='15dp',
                                    pos_hint={'center_x': 1, 'center_y': .5})
        self.checkbox_default_server = CheckBox(
                            size_hint=(.1, 1))
        self.checkbox_default_server.bind(on_press=self.checkbox_default_server_click)

        self.checkbox_default_server_layout.add_widget(self.checkbox_default_server_label)
        self.checkbox_default_server_layout.add_widget(self.checkbox_default_server)
        
        self.b1_label = LeftAlignedLabel(text='DATABASE ADDRESS')
        self.b1_input = RoundedTextInput()
        self.b2_label = LeftAlignedLabel(text='DATABASE PORT')
        self.b2_input = RoundedTextInput()
        self.b3_label = LeftAlignedLabel(text='DATABASE LOGIN')
        self.b3_input = RoundedTextInput()
        self.b4_label = LeftAlignedLabel(text='DATABASE PASSWORD')
        self.b4_input = RoundedTextInput()
        self.b5_label = LeftAlignedLabel(text='ENCRYPTION PASSWORD')
        self.b5_input = RoundedTextInput()

        self.button = RoundedButton(
                            text='LOGIN',
                            size_hint=(.95, .17),
                            font_size='25dp',
                            bold=True,
                            pos_hint={"center_x": .5, "center_y": 1})
                            
        self.button.bind(on_press = self.login)

        # Margins
        self.login1_margin_label = Label(text='', size_hint=(.1, .1))
        self.login2_margin_label = Label(text='', size_hint=(.1, .01))
        self.login3_margin_label = Label(text='', size_hint=(.1, .5))
        
        # Create Layout 
        self.main_layout.add_widget(self.login_layout)

        self.login_layout.add_widget(self.login1_margin_label)
        self.login_layout.add_widget(self.logo)
        self.login_layout.add_widget(self.main_label)
        self.login_layout.add_widget(self.info_label)
        self.login_layout.add_widget(self.b1_label)
        self.login_layout.add_widget(self.b1_input)
        self.login_layout.add_widget(self.b2_label)
        self.login_layout.add_widget(self.b2_input)
        self.login_layout.add_widget(self.checkbox_default_server_layout)
        self.login_layout.add_widget(self.b3_label)
        self.login_layout.add_widget(self.b3_input)
        self.login_layout.add_widget(self.b4_label)
        self.login_layout.add_widget(self.b4_input)
        self.login_layout.add_widget(self.b5_label)
        self.login_layout.add_widget(self.b5_input)
        self.login_layout.add_widget(self.login2_margin_label)
        self.login_layout.add_widget(self.button)
        self.login_layout.add_widget(self.login3_margin_label)

        return self.main_layout

class RoundedButton(Button): pass
class RoundedTextInput(TextInput): pass
class LeftAlignedLabel(Label): pass
class RightAlignedLabel(Label): pass
class ElementTextInput(TextInput): pass
class SearchInput(TextInput): pass
class DeleteButton(Button): pass
class BorderImage(Image): pass
class RoundedButtonDelete(Button): pass
class ElementTitle(Label): pass

if __name__ == '__main__':
    app = MainApp()
    app.run()