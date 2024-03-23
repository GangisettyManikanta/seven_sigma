import os

from anvil.tables import app_tables
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.spinner import SpinnerOption
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
import anvil.server
from homepage import MainScreen
from borrower_dashboard import DashboardScreen
from lender_dashboard import LenderDashboard
anvil.server.connect("server_PB72N67CPKFT7OZAZOOXOJEE-4YOBZHMRNHA2HC4Q")
import configparser
# Initialize configuration
config = configparser.ConfigParser()
class MyApp(MDApp):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())

        # Check user configuration
        if self.check_user_config():
            user_type = config.get('USER', 'user_type')
            if user_type == 'borrower':
                dashboard_screen = DashboardScreen(name='DashboardScreen')
            elif user_type == 'lender':
                dashboard_screen = LenderDashboard(name='LenderDashboard')
            sm.add_widget(dashboard_screen)
        else:
            main_screen = MainScreen(name='MainScreen')
            sm.add_widget(main_screen)

        SpinnerOption.font_size = dp(10.5)
        SpinnerOption.background_color = [0.2, 0.4, 0.6, 1]
        SpinnerOption.font_name = "Roboto-Bold"

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
        product_groups = app_tables.fin_product_details.search()

        # Extract unique product groups
        unique_groups = set(product['product_group'] for product in product_groups)

        # Update the Spinner with unique product groups
        spinner = self.root.get_screen('NewloanScreen').ids.group_id1
        spinner.values = list(unique_groups)
        # Clear other Spinners and labels
        self.clear_spinners_and_labels(['group_id2', 'group_id3'])
        self.clear_label('product_description')

    def fetch_product_categories(self):
        # Clear other Spinners and labels
        self.clear_spinners_and_labels(['group_id3'])
        self.clear_label('product_description')

        # Get the selected product group
        selected_group = self.root.get_screen('NewloanScreen').ids.group_id1.text

        # Call the server function using Anvil Uplink to filter categories based on the selected group
        product_categories = app_tables.fin_product_details.search(product_group=selected_group)

        # Extract unique product categories for the selected group
        unique_categories = set(product['product_categories'] for product in product_categories)

        # Update the Spinner with unique product categories
        spinner = self.root.get_screen('NewloanScreen').ids.group_id2
        spinner.values = list(unique_categories)

    def fetch_product_name(self):
        # Clear other Spinners and labels
        self.clear_label('product_description')

        # Get the selected product category
        selected_category = self.root.get_screen('NewloanScreen').ids.group_id2.text

        # Call the server function using Anvil Uplink to filter product names based on the selected category
        product_names = app_tables.fin_product_details.search(product_categories=selected_category)

        # Extract unique product names for the selected category
        unique_names = set(product['product_name'] for product in product_names)

        # Update the Spinner with unique product names
        spinner = self.root.get_screen('NewloanScreen').ids.group_id3
        spinner.values = list(unique_names)
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
                self.root.get_screen('NewloanScreen').ids.product_description.text = product[0]['product_description']
        else:
            # Clear the product description label if no product description is found
            self.root.get_screen('NewloanScreen').ids.product_description.text = ""

    def clear_spinners_and_labels(self, spinner_ids):
        for spinner_id in spinner_ids:
            self.root.get_screen('NewloanScreen').ids[spinner_id].text = "Select"
            self.root.get_screen('NewloanScreen').ids[spinner_id].values = []

    def clear_label(self, label_id):
        self.root.get_screen('NewloanScreen').ids[label_id].text = ""
    def on_start(self):
        Window.softinput_mode = "below_target"

    def check_user_config(self):
        # Check if config file exists
        if not os.path.exists('config.ini'):
            return False

        # Read config file
        config.read('config.ini')

        # Check if 'USER' section exists and required fields are present
        if 'USER' in config and 'email' in config['USER'] and 'user_type' in config['USER'] and 'logged_in' in config[
            'USER']:
            return config.getboolean('USER', 'logged_in')

        return False

class MyScreenManager(ScreenManager):
    pass


if __name__ == '__main__':
    MyApp().run()