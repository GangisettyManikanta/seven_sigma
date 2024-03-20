from anvil.tables import app_tables
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.spinner import SpinnerOption
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from homepage import MainScreen
import anvil.server
anvil.server.connect("server_DDFFDPCYFLU7YEUB7AKS3ES2-3PQ3UW72AZJGD2JJ")

class MyApp(MDApp):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        main_screen = MainScreen(name='MainScreen')
        SpinnerOption.font_size = dp(10.5)
        SpinnerOption.background_color = [0.2, 0.4, 0.6, 1]
        SpinnerOption.font_name = "Roboto-Bold"
        sm.add_widget(main_screen)

        return sm

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        # Preload data when the app starts
        self.fetch_product_groups()

    def fetch_product_groups(self):
        # Call the server function using Anvil Uplink
        product_group = app_tables.fin_product_group.search()
        # Process the data as per your requirement, for example, update the Spinner with fetched usernames
        spinner = self.root.get_screen('NewloanScreen').ids.group_id1
        spinner.values = [user['name'] for user in product_group]

    def fetch_product_categories(self):
        # Get the selected product group
        selected_group = self.root.get_screen('NewloanScreen').ids.group_id1.text
        # Call the server function using Anvil Uplink to filter categories based on the selected group
        product_categories = app_tables.fin_product_categories.search(name_group=selected_group)
        # Update the Spinner with filtered categories
        spinner = self.root.get_screen('NewloanScreen').ids.group_id2
        spinner.values = [user['name_categories'] for user in product_categories]

    def fetch_product_name(self):
        # Get the selected product category
        selected_category = self.root.get_screen('NewloanScreen').ids.group_id2.text
        # Call the server function using Anvil Uplink to filter product names based on the selected category
        product_name = app_tables.fin_product_details.search(product_categories=selected_category)
        # Update the Spinner with filtered product names
        spinner = self.root.get_screen('NewloanScreen').ids.group_id3
        spinner.values = [user['product_name'] for user in product_name]
        # Clear product description label when selecting a new product name
        self.root.get_screen('NewloanScreen').ids.product_description.text = ""
        # Fetch product description
        self.fetch_product_description()
        # Fetch product ID
        self.fetch_product_id()

    def fetch_emi_type(self):
        # Get the selected product category
        selected_category = self.root.get_screen('NewloanScreen').ids.group_id3.text
        # Call the server function using Anvil Uplink to filter product names based on the selected category
        emi_type = app_tables.fin_product_details.search(product_name=selected_category)
        # Extract emi_type from the fetched data
        if emi_type:
            emi_type_list = emi_type[0]['emi_payment'].split(',')  # Split the emi_type string by commas
            # Update the Spinner with filtered product names
            spinner = self.root.get_screen('NewloanScreen1').ids.group_id4
            spinner.values = emi_type_list
        else:
            # Clear the Spinner if no emi_type is found
            self.root.get_screen('NewloanScreen1').ids.group_id4.values = []

    def fetch_product_description(self):
        # Get the selected product name
        selected_product_name = self.root.get_screen('NewloanScreen').ids.group_id3.text
        # Call the server function using Anvil Uplink to fetch the product description based on the selected product name
        product = app_tables.fin_product_details.search(product_name=selected_product_name)
        # Check if product list is not empty before accessing its elements
        if product:
            if len(product) > 0:
                # Update the product description label with the fetched description
                self.root.get_screen('NewloanScreen').ids.product_description.text = product[0]['product_discription']
        else:
            # Clear the product description label if no product description is found
            self.root.get_screen('NewloanScreen').ids.product_description.text = ""

    def fetch_product_id(self):
        # Get the selected product name
        selected_product_name = self.root.get_screen('NewloanScreen').ids.group_id3.text
        # Call the server function using Anvil Uplink to fetch the product ID based on the selected product name
        product = app_tables.fin_product_details.search(product_name=selected_product_name)
        # Check if product list is not empty before accessing its elements
        if product:
            if len(product) > 0:
                # Update the product ID label with the fetched product ID
                self.root.get_screen('NewloanScreen').ids.product_id.text = str(product[0]['product_id'])
        else:
            # Clear the product ID label if no product ID is found
            self.root.get_screen('NewloanScreen').ids.product_id.text = ""

    def on_start(self):
        Window.softinput_mode = "below_target"


class MyScreenManager(ScreenManager):
    pass


if __name__ == '__main__':
    MyApp().run()