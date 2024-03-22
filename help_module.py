from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import SlideTransition

Builder.load_string(
    """
<WindowManager>:
    HelpScreen:
    FirstScreen:
    SecondScreen:
    ThirdScreen:
    FourthScreen:
    FifthScreen:
    SixthScreen:
    SeventhScreen:
    EighthScreen:
    NinthScreen:
    TenthScreen:
    EleventhScreen:
    TwelveScreen:
    ThirteenScreen:
    FourteenScreen:

<HelpScreen>:
    name: 'HelpScreen'
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Help Center"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left',lambda x: root.go_back()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        MDScrollView:
            BoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                OneLineListItem:
                    id: item1
                    text: "How to apply for Loan ?"
                    on_release: root.first_screen()

                OneLineListItem:
                    id: item2
                    text: "How about charges ? "
                    on_release: root.second_screen()
                    
                OneLineListItem:
                    id: item3
                    text: "How to do payments ?"
                    on_release: root.third_screen()

                OneLineListItem:
                    id: item4
                    text: "How to check loan status ?"
                    on_release: root.fourth_screen()
                    

                OneLineListItem:
                    id: item5
                    text: " where do you find transaction History ?"
                    on_release: root.fifth_screen()
                OneLineListItem:
                    id: item6
                    text: "How to add money to wallet ?"
                    on_release: root.sixth_screen()
                OneLineListItem:
                    id: item7
                    text: "What is the maximum amount for applying loan ?"
                    on_release: root.seventh_screen()
                OneLineListItem:
                    id: item8
                    text: "How to invest Money in GP2P Platform ?"
                    on_release: root.eighth_screen()
                OneLineListItem:
                    id: item9
                    text: "How can platform provide security ?"
                    on_release: root.ninth_screen()
                OneLineListItem:
                    id: item10
                    text: "How much time do you take to disburse the loans ?"
                    on_release: root.tenth_screen()
                OneLineListItem:
                    id: item11
                    text: "How much time do you take to disburse the loans ?"
                    on_release: root.eleventh_screen()
                OneLineListItem:
                    id: item12
                    text: "How easy to get out ?"
                    on_release: root.twelve_screen()
                OneLineListItem:
                    id: item13
                    text: "How much returns I can except ?"
                    on_release: root.thirteenth_screen()
                OneLineListItem:
                    id: item14
                    text: "How many types of loans GP2P provides?"
                    on_release: root.fourteenth_screen()
                    

<FirstScreen>:
    name: 'FirstScreen'
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Help center"
            elevation: 2
            md_bg_color: 0.043, 0.145, 0.278, 1
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            MDLabel:
                text: "Open New Loan Request --> "
                halign: "center"
                

<SecondScreen>:
    name: 'SecondScreen'  # Corrected screen name
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Help Center"
            elevation: 2
            md_bg_color: 0.043, 0.145, 0.278, 1
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            MDLabel:
                text:"Welcome to GP2P. With GP2P, you will get fast,loans "
                halign:"center"
                
<ThirdScreen>:
    name: 'ThirdScreen'  # Corrected screen name
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Help Center"
            elevation: 2
            md_bg_color: 0.043, 0.145, 0.278, 1
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            MDLabel:
                text:"Welcome to GP2P. With GP2P, you will get fast,loans "
                halign:"center"


<FourthScreen>:
    name: 'FourthScreen'  # Corrected screen name
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Help Center"
            elevation: 2
            md_bg_color: 0.043, 0.145, 0.278, 1
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            MDLabel:
                text:"Welcome to GP2P. With GP2P, you will get fast,loans "
                halign:"center"

<FifthScreen>:
    name: 'FifthScreen'  # Corrected screen name
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Help Center"
            elevation: 2
            md_bg_color: 0.043, 0.145, 0.278, 1
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            MDLabel:
                text:"Welcome to GP2P. With GP2P, you will get fast,loans "
                halign:"center"

<SixthScreen>:
    name: 'SixthScreen'  # Corrected screen name
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Help Center"
            elevation: 2
            md_bg_color: 0.043, 0.145, 0.278, 1
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            MDLabel:
                text:"Welcome to GP2P. With GP2P, you will get fast,loans "
                halign:"center"

<SeventhScreen>:
    name: 'SeventhScreen'  # Corrected screen name
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Help Center"
            elevation: 2
            md_bg_color: 0.043, 0.145, 0.278, 1
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            MDLabel:
                text:"Welcome to GP2P. With GP2P, you will get fast,loans "
                halign:"center"

<EighthScreen>:
    name: 'EighthScreen'  # Corrected screen name
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Help Center"
            elevation: 2
            md_bg_color: 0.043, 0.145, 0.278, 1
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            MDLabel:
                text:"Welcome to GP2P. With GP2P, you will get fast,loans "
                halign:"center"

<NinthScreen>:
    name: 'NinthScreen'  # Corrected screen name
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Help Center"
            elevation: 2
            md_bg_color: 0.043, 0.145, 0.278, 1
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            MDLabel:
                text:"Welcome to GP2P. With GP2P, you will get fast,loans "
                halign:"center"

<TenthScreen>:
    name: 'TenthScreen'  # Corrected screen name
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Help Center"
            elevation: 2
            md_bg_color: 0.043, 0.145, 0.278, 1
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            MDLabel:
                text:"Welcome to GP2P. With GP2P, you will get fast,loans "
                halign:"center"

<EleventhScreen>:
    name: 'EleventhScreen'  # Corrected screen name
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Help Center"
            elevation: 2
            md_bg_color: 0.043, 0.145, 0.278, 1
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            MDLabel:
                text:"Welcome to GP2P. With GP2P, you will get fast,loans "
                halign:"center"

<TwelveScreen>:
    name: 'TwelveScreen'  # Corrected screen name
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Help Center"
            elevation: 2
            md_bg_color: 0.043, 0.145, 0.278, 1
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            MDLabel:
                text:"Welcome to GP2P. With GP2P, you will get fast,loans "
                halign:"center"

<ThirteenScreen>:
    name: 'ThirteenScreen'  # Corrected screen name
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Help Center"
            elevation: 2
            md_bg_color: 0.043, 0.145, 0.278, 1
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            MDLabel:
                text:"Welcome to GP2P. With GP2P, you will get fast,loans "
                halign:"center"

<FourteenScreen>:
    name: 'FourteenScreen'  # Corrected screen name
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Help Center"
            elevation: 2
            md_bg_color: 0.043, 0.145, 0.278, 1
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            MDLabel:
                text:"Welcome to GP2P. With GP2P, you will get fast,loans "
                halign:"center"





"""

)


class HelpScreen(Screen):
    def go_back(self):
        pass

    def first_screen(self):
        sm = self.manager
        borrower_screen = FirstScreen(name='FirstScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'FirstScreen'

    def second_screen(self):
        sm = self.manager
        borrower_screen = SecondScreen(name='SecondScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'SecondScreen'

    def third_screen(self):
        sm = self.manager
        borrower_screen = ThirdScreen(name='ThirdScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'ThirdScreen'

    def fourth_screen(self):
        sm = self.manager
        borrower_screen = FourthScreen(name='FourthScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'FourthScreen'

    def fifth_screen(self):
        sm = self.manager
        borrower_screen = FifthScreen(name='FifthScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'FifthScreen'

    def sixth_screen(self):
        sm = self.manager
        borrower_screen = SixthScreen(name='SixthScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'SixthScreen'

    def seventh_screen(self):
        sm = self.manager
        borrower_screen = SeventhScreen(name='SeventhScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'SeventhScreen'

    def eighth_screen(self):
        sm = self.manager
        borrower_screen = EighthScreen(name='EighthScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'EighthScreen'

    def ninth_screen(self):
        sm = self.manager
        borrower_screen = NinthScreen(name='NinthScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'NinthScreen'

    def tenth_screen(self):
        sm = self.manager
        borrower_screen = TenthScreen(name='TenthScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'TenthScreen'

    def eleventh_screen(self):
        sm = self.manager
        borrower_screen = EleventhScreen(name='EleventhScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'EleventhScreen'

    def twelve_screen(self):
        sm = self.manager
        borrower_screen = TwelveScreen(name='TwelveScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'TwelveScreen'

    def thirteenth_screen(self):
        sm = self.manager
        borrower_screen = ThirteenScreen(name='ThirteenScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'ThirteenScreen'

    def fourteenth_screen(self):
        sm = self.manager
        borrower_screen = FourteenScreen(name='FourteenScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'FourteenScreen'


class FirstScreen(Screen):
    def go_back(self):
        self.manager.current = 'HelpScreen'


class SecondScreen(Screen):
    def go_back(self):
        self.manager.current = 'HelpScreen'


class ThirdScreen(Screen):
    def go_back(self):
        self.manager.current = 'HelpScreen'


class FourthScreen(Screen):
    def go_back(self):
        self.manager.current = 'HelpScreen'


class FifthScreen(Screen):
    def go_back(self):
        self.manager.current = 'HelpScreen'


class SixthScreen(Screen):
    def go_back(self):
        self.manager.current = 'HelpScreen'


class SeventhScreen(Screen):
    def go_back(self):
        self.manager.current = 'HelpScreen'


class EighthScreen(Screen):
    def go_back(self):
        self.manager.current = 'HelpScreen'


class NinthScreen(Screen):
    def go_back(self):
        self.manager.current = 'HelpScreen'


class TenthScreen(Screen):
    def go_back(self):
        self.manager.current = 'HelpScreen'


class EleventhScreen(Screen):
    def go_back(self):
        self.manager.current = 'HelpScreen'


class TwelveScreen(Screen):
    def go_back(self):
        self.manager.current = 'HelpScreen'


class ThirteenScreen(Screen):
    def go_back(self):
        self.manager.current = 'HelpScreen'


class FourteenScreen(Screen):
    def go_back(self):
        self.manager.current = 'HelpScreen'


class MyScreenManager(ScreenManager):
    pass
