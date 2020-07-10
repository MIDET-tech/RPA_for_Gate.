# Summary of modules

import os
import time
import glob
import codecs
import pyperclip
import pyautogui as pg
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class modules:
    def __init__(self,username,driver):
        self.username = username
        self.driver = driver
    
    def format_changer(self):
        # Changing file format 
        Shift_JIS_csv_path = "C:\\Users\\{}\\RPA_for_Gate.-master\\data_shift_jis.csv".format(self.username)    
        utf8_csv_path = "C:\\Users\\{}\\RPA_for_Gate.-master\\data_utf-8.csv".format(self.username)

        # Shift-JIS→utf-8
        file_Shift_JIS = codecs.open(Shift_JIS_csv_path, "r", "Shift_JIS")
        file_utf = codecs.open(utf8_csv_path, "w", "utf-8")
        for row in file_Shift_JIS:
            file_utf.write(row)
        file_Shift_JIS.close()
        file_utf.close()

    def login(self):
        # Make sure to replace email address and password
        self.driver.get("https://gate.estate/service/planner/signin?next_url=%2Fplanner%2Fselect")

        self.driver.maximize_window()

        WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located)

        time.sleep(1)
        
        email = self.driver.find_element_by_css_selector("#mat-input-2")
        email.send_keys("YOUR_EMAIL_ADDRESS")

        password = self.driver.find_element_by_css_selector("#mat-input-0")
        password.send_keys("YOUR_PASSWORD")
   
        button_1 = self.driver.find_element_by_css_selector("body > app-root > app-login-widget > div > form > div:nth-child(2) > mat-form-field > div > div.mat-form-field-flex > div > div > button")
        button_1.click()

        time.sleep(7)

        button_2 = self.driver.find_element_by_css_selector("body > app-root > app-dashboard-layout > div > div.container > app-gate-product-widget > div > div > div > div.content > div:nth-child(4) > div.action > button")
        button_2.click()

        time.sleep(10)
    
    def sample(self):
        print(y)
        print(bukken_data[3])
        
    def property_information(self,y,bukken_data):
        self.y = y
        self.bukken_data = bukken_data
        
        assessment_register = self.driver.find_element_by_css_selector("#select-estate-view > div.select-estate-content > div:nth-child(2) > div > ul > li:nth-child(3)")
        assessment_register.click()

        time.sleep(2)
        
        # Prefecture
        pref_code = self.driver.find_element_by_name("pref_code")
        select_pref_code = Select(pref_code)
        select_pref_code.select_by_visible_text(self.bukken_data[self.y][1])

        time.sleep(3)
        
        # Cities
        city = self.driver.find_element_by_name("city")
        select_city = Select(city)
        select_city.select_by_visible_text(self.bukken_data[self.y][2])
        
        # Town
        town = self.driver.find_element_by_name("aza")
        town.send_keys(self.bukken_data[self.y][3])
        
        # Address
        chome = self.driver.find_element_by_name("chome")
        chome.send_keys(self.bukken_data[self.y][4])
        chiban1 = self.driver.find_element_by_name("chiban1")
        chiban1.send_keys(self.bukken_data[self.y][5])
        chiban2 = self.driver.find_element_by_name("chiban2")
        chiban2.send_keys(self.bukken_data[self.y][6])
        
        # Nearest station
        for k in range(int(self.bukken_data[self.y][30])):
            railway = self.driver.find_element_by_css_selector("#private-estate-form-view > div > div > form > ul > li.row.railways > div > ul:nth-child({}) > li.item.line > select".format(k+1))
            select_railway = Select(railway)
            select_railway.select_by_visible_text(self.bukken_data[self.y][31+3*k])

            time.sleep(2)

            station = self.driver.find_element_by_css_selector("#private-estate-form-view > div > div > form > ul > li.row.railways > div > ul:nth-child({}) > li.item.station > select".format(k+1))
            select_station = Select(station)
            select_station.select_by_visible_text(self.bukken_data[self.y][32+3*k])

            time_to_reach = self.driver.find_element_by_css_selector("#private-estate-form-view > div > div > form > ul > li.row.railways > div > ul:nth-child({}) > li.item.minutes > input".format(k+1))
            time_to_reach.send_keys(self.bukken_data[self.y][33+3*k])

            more_station = self.driver.find_element_by_css_selector("#private-estate-form-view > div > div > form > ul > li.row.railways > div > ul > li.item.add.ng-scope > a")
            more_station.click()

            time.sleep(2)
            
        # Name of the building
        estate_name = self.driver.find_element_by_name("estate_name")
        estate_name.send_keys(self.bukken_data[self.y][7])
        
        # Building Structure
        kouzou_dic = {"SRC":"1", "RC":"2", "鉄骨":"3", "木造":"4"}
        kouzou_1 = kouzou_dic[self.bukken_data[self.y][8]]

        kouzou_2 = self.driver.find_element_by_css_selector("#private-estate-form-view > div > div > form > ul > li.row.building_structure > div > div > label:nth-child({})".format(kouzou_1))
        kouzou_2.click()
        
        # Age of the building
        year = self.driver.find_element_by_css_selector("#private-estate-form-view > div > div > form > ul > li.row.built_date > div > ul > li.item.year > select")
        select_year = Select(year)
        select_year.select_by_value("number:" + self.bukken_data[self.y][9])

        month = self.driver.find_element_by_css_selector("#private-estate-form-view > div > div > form > ul > li.row.built_date > div > ul > li.item.months > select")
        select_month = Select(month)
        select_month.select_by_value("number:" + self.bukken_data[self.y][10])
        
        # Number of rooms
        number_of_houses = self.driver.find_element_by_name("number_of_houses")
        number_of_houses.send_keys(self.bukken_data[self.y][11])
        
        # Number of floors
        number_of_floors = self.driver.find_element_by_name("number_of_floors")
        number_of_floors.send_keys(self.bukken_data[self.y][12])
        
        # Expected selling price
        expected_selling_price = self.driver.find_element_by_name("expected_selling_price")
        expected_selling_price.send_keys(self.bukken_data[self.y][13])
        
        # Located floor
        floor_located = self.driver.find_element_by_name("floor_located")
        floor_located.send_keys(self.bukken_data[self.y][14])
        
        # Occupation area
        occupation_area = self.driver.find_element_by_name("occupation_area")
        occupation_area.send_keys(self.bukken_data[self.y][15])

        # Layout of rooms
        layout_rooms = self.driver.find_element_by_name("layout_rooms")
        layout_rooms.send_keys("1")

        layout_dic = {"R":"1", "K":"2", "D":"3", "L":"4"}
        layout_data_list = list(self.bukken_data[self.y][16])
        lay = layout_dic[layout_data_list[1]]

        layout = self.driver.find_element_by_css_selector("#private-estate-form-view > div > div > form > ul > li.row.layout_rooms > div > div > label:nth-child({})".format(lay))
        layout.click()
        
        # Rent
        months_rent = self.driver.find_element_by_name("months_rent")
        months_rent.send_keys(self.bukken_data[self.y][17])
        
        # Management fees per month
        months_management_fees = self.driver.find_element_by_name("months_management_fees")
        months_management_fees.send_keys(self.bukken_data[self.y][18])
        
        # Repair reserve fund fees per month
        months_repair_reserve_fund_fees = self.driver.find_element_by_name("months_repair_reserve_fund_fees")
        months_repair_reserve_fund_fees.send_keys(self.bukken_data[self.y][19])
        
        # Click advanced setting
        advanced_settings = self.driver.find_element_by_css_selector("#private-estate-form-view > div > div > form > ul > li.row.optional-label > span:nth-child(1)")
        advanced_settings.click()
        
        # Other management fees per month
        months_other_management_fees = self.driver.find_element_by_name("months_other_management_fees")
        months_other_management_fees.send_keys(self.bukken_data[self.y][20])

        # Room number
        room_number = self.driver.find_element_by_name("room_number")
        room_number.send_keys(self.bukken_data[self.y][21])
        
        # Property tax
        property_tax = self.driver.find_element_by_name("property_tax")
        property_tax.send_keys(self.bukken_data[self.y][22])
        
        # Finish
        finish_1 = self.driver.find_element_by_css_selector("#private-estate-form-view > div > div > form > div > button")
        finish_1.click()

        time.sleep(10)

        finish_2 = self.driver.find_element_by_css_selector("#private-estate-form-view > aside > div > div > button")
        finish_2.click()

        time.sleep(5)
        
    def GateMarketSurvey(self,username):
        self.username = username
        
        market = self.driver.find_element_by_css_selector("#estate-container > li:nth-child(1) > div > div:nth-child(1) > a.market-survey-btn.btn.btn-sm")
        market.click()

        time.sleep(20)

        handle_array_10 = self.driver.window_handles
        self.driver.switch_to.window(handle_array_10[-1])

        time.sleep(3)

        market_2 = self.driver.find_element_by_css_selector("body > app-root > app-market-survey-layout > div > header > div > div.print-tool > div")
        market_2.click()

        time.sleep(3)

        market_3 = self.driver.find_element_by_css_selector("#mat-dialog-0 > app-show-modal-print-widget > div.mat-dialog-actions > button.estate-bg-blue.no-rounded.printbutton.mat-raised-button")
        market_3.click()
        
        date_now = datetime.now().strftime("%H%M")
        
        time.sleep(10)
        
        market_4 = self.driver.find_element_by_css_selector("#mat-dialog-1 > app-show-modal-print-preview-widget > div.mat-dialog-actions > button.estate-bg-blue.mat-raised-button")
        market_4.click()
        
        time.sleep(20)
        
        # Change filename
        name_of_building = self.bukken_data[self.y][7]
        
        path = "C:\\Users\\{}\\Downloads\\*".format(self.username) + date_now + ".pdf"
        file_list = glob.glob(path)
        before = file_list[0]
        after =  "C:\\Users\\{}\\Downloads\\{}_GateMarketSurvey.pdf".format(self.username, name_of_building)

        os.rename(before, after)

        time.sleep(10)
        
    def detailed_information(self,y,bukken_data):
        self.y = y
        self.bukken_data = bukken_data
        
        touroku = self.driver.find_element_by_css_selector("#estate-container > li:nth-child(1) > a")
        touroku.click()

        time.sleep(15)

        handle_array = self.driver.window_handles
        self.driver.switch_to.window(handle_array[-1])
        
        new = self.driver.find_element_by_css_selector("#planner-view > div > nav.side.nopointer.ng-scope > header > button > div > span")
        new.click()

        time.sleep(3)
        
        #vacancy rate
        if len(self.bukken_data[self.y][23]) != 0:
            vacancy_rate = self.bukken_data[self.y][23]
        else:
            number = self.driver.find_element_by_css_selector("#numerical_box_vacancy_rate_modal-spinner")
            default = number.get_attribute("value")
            vacancy_rate = str(default)
        
        vacancy_rate_list = list(vacancy_rate)
        numerical_box_vacancy_rate_modal_spinner = self.driver.find_element_by_id("numerical_box_vacancy_rate_modal-spinner")
        numerical_box_vacancy_rate_modal_spinner.click()
        numerical_box_vacancy_rate_modal_spinner.clear()
        
        if len(vacancy_rate_list) == 4:
            vacancy_rate_1 =vacancy_rate_list[0]
            numerical_box_vacancy_rate_modal_spinner.send_keys(vacancy_rate_1)
            time.sleep(1)
            vacancy_rate_2 = vacancy_rate_list[1]
            numerical_box_vacancy_rate_modal_spinner.send_keys(vacancy_rate_2)
            time.sleep(1)
            vacancy_rate_3 = vacancy_rate_list[3]
            numerical_box_vacancy_rate_modal_spinner.send_keys(vacancy_rate_3)
            time.sleep(1)
            numerical_box_vacancy_rate_modal_spinner.send_keys(Keys.LEFT)
            time.sleep(1)
            vacancy_rate_4 = vacancy_rate_list[2]
            numerical_box_vacancy_rate_modal_spinner.send_keys(vacancy_rate_4)
            time.sleep(1)
        elif len(vacancy_rate_list) == 3:
            vacancy_rate_1 = vacancy_rate_list[0]
            numerical_box_vacancy_rate_modal_spinner.send_keys(vacancy_rate_1)
            time.sleep(1)
            vacancy_rate_2 = vacancy_rate_list[1]
            numerical_box_vacancy_rate_modal_spinner.send_keys(vacancy_rate_2)
            time.sleep(1)
            vacancy_rate_3 = vacancy_rate_list[2]
            numerical_box_vacancy_rate_modal_spinner.send_keys(vacancy_rate_3)
            time.sleep(1)
        else:
            vacancy_rate_1 = vacancy_rate_list[0]
            numerical_box_vacancy_rate_modal_spinner.send_keys(vacancy_rate_1)
            time.sleep(1)
            
        # Extra expenses
        extra_expenses = self.bukken_data[self.y][24]
        extra_expenses_list = list(extra_expenses)
        numerical_box_initial_expense_modal_spinner = self.driver.find_element_by_id("numerical_box_initial_expense_modal-spinner")
        numerical_box_initial_expense_modal_spinner.click()
        numerical_box_initial_expense_modal_spinner.clear()
        for i in range(len(extra_expenses_list)):
            extra_expenses_1 = int(i)
            extra_expenses_2 = extra_expenses_list[extra_expenses_1]
            numerical_box_initial_expense_modal_spinner.send_keys(extra_expenses_2)
            time.sleep(0.5) 

        time.sleep(0.3)
        
        # Personal funds
        personal_funds = self.bukken_data[self.y][25]
        personal_funds_list = list(personal_funds)
        numerical_box_personal_funds_modal_spinner = self.driver.find_element_by_id("numerical_box_personal_funds_modal-spinner")
        numerical_box_personal_funds_modal_spinner.click()
        numerical_box_personal_funds_modal_spinner.clear()
        for i in range(len(personal_funds_list)):
            personal_funds_1 = int(i)
            personal_funds_2 = personal_funds_list[personal_funds_1]
            numerical_box_personal_funds_modal_spinner.send_keys(personal_funds_2)
            time.sleep(0.5)

        time.sleep(0.3) 
        
        # Interest rate
        interest_rate = self.bukken_data[self.y][26]
        interest_rate_list = list(interest_rate)
        numerical_box_interest_rate_modal_spinner = self.driver.find_element_by_id("numerical_box_interest_rate_modal-spinner")
        numerical_box_interest_rate_modal_spinner.click()
        numerical_box_interest_rate_modal_spinner.clear()
        for i in range(len(interest_rate_list)):
            interest_rate_1 = int(i)
            interest_rate_2 = interest_rate_list[interest_rate_1]
            numerical_box_interest_rate_modal_spinner.send_keys(interest_rate_2)
            time.sleep(0.5)

        time.sleep(0.3)
        
        # Repayment period
        repayment_period = self.bukken_data[self.y][27]
        repayment_period_list = list(repayment_period)
        numerical_box_repayment_period_modal_spinner = self.driver.find_element_by_id("numerical_box_repayment_period_modal-spinner")
        numerical_box_repayment_period_modal_spinner.click()
        numerical_box_repayment_period_modal_spinner.clear()
        for i in range(len(repayment_period_list)):
            repayment_period_1 = int(i)
            repayment_period_2 = repayment_period_list[repayment_period_1]
            numerical_box_repayment_period_modal_spinner.send_keys(repayment_period_2)
            time.sleep(0.5)

        time.sleep(0.3)
        
        # Sold year
        sold_year = self.bukken_data[self.y][28]
        sold_year_list = list(sold_year)
        numerical_box_sold_year_modal_spinner = self.driver.find_element_by_id("numerical_box_sold_year_modal-spinner")
        numerical_box_sold_year_modal_spinner.click()
        numerical_box_sold_year_modal_spinner.clear()
        for i in range(len(sold_year_list)):
            sold_year_1 = int(i)
            sold_year_2 = sold_year_list[sold_year_1]
            numerical_box_sold_year_modal_spinner.send_keys(sold_year_2)
            time.sleep(0.5)

        time.sleep(0.3)

        # Egi rate for management commision expense
        numerical_box_egi_rate_for_management_commision_expense_modal_spinner = self.driver.find_element_by_id("numerical_box_egi_rate_for_management_commision_expense_modal-spinner")
        numerical_box_egi_rate_for_management_commision_expense_modal_spinner.click()
        numerical_box_egi_rate_for_management_commision_expense_modal_spinner.clear()

        if len(self.bukken_data[self.y][29]) != 0:
            commision_expense = int(self.bukken_data[self.y][17]) * (1-(float(vacancy_rate) / 100))
            commision_expense_1 = (int(self.bukken_data[self.y][29])*100) / commision_expense
            commision_expense_2 = round(commision_expense_1,2)
            commision_expense_2_list = list(str(commision_expense_2))
        else:
            commision_expense = self.driver.find_element_by_css_selector("#numerical_box_egi_rate_for_management_commision_expense_modal-spinner")
            commision_expense_1 = commision_expense.get_attribute("value")
            commision_expense_2 = str(commision_expense_1)
            commision_expense_2_list = list(commision_expense_2)


        if len(commision_expense_2_list) == 4:
            commision_expense_3 = commision_expense_2_list[0]
            numerical_box_egi_rate_for_management_commision_expense_modal_spinner.send_keys(commision_expense_3)
            time.sleep(1)
            commision_expense_4 = commision_expense_2_list[1]
            numerical_box_egi_rate_for_management_commision_expense_modal_spinner.send_keys(commision_expense_4)
            time.sleep(1)
            commision_expense_5 = commision_expense_2_list[3]
            numerical_box_egi_rate_for_management_commision_expense_modal_spinner.send_keys(commision_expense_5)
            time.sleep(1)
            numerical_box_egi_rate_for_management_commision_expense_modal_spinner.send_keys(Keys.LEFT)
            time.sleep(1)
            commision_expense_6 = commision_expense_2_list[2]
            numerical_box_egi_rate_for_management_commision_expense_modal_spinner.send_keys(commision_expense_6)
            time.sleep(1)
        elif len(commision_expense_2_list) == 3:
            commision_expense_3 = commision_expense_2_list[0]
            numerical_box_egi_rate_for_management_commision_expense_modal_spinner.send_keys(commision_expense_3)
            time.sleep(1)
            commision_expense_4 = commision_expense_2_list[1]
            numerical_box_egi_rate_for_management_commision_expense_modal_spinner.send_keys(commision_expense_4)
            time.sleep(1)
            commision_expense_5 = commision_expense_2_list[2]
            numerical_box_egi_rate_for_management_commision_expense_modal_spinner.send_keys(commision_expense_5)
            time.sleep(1)    

        time.sleep(0.3)
        
        # Finish
        finish_3 = self.driver.find_element_by_css_selector("#planner-settings-modal > div > div.modal-footer > div > div.col-xs-4.text-center > button")
        finish_3.click()

        time.sleep(15)
        
        # Change sold year caprate
        sold_year_caprate = self.driver.find_element_by_css_selector("#appendix > div > div > div:nth-child(1) > div:nth-child(2) > p > span:nth-child(3)")
        sold_year_caprate_1 = str(sold_year_caprate.text)
        sold_year_caprate_1_list = list(sold_year_caprate_1)

        new_2 = self.driver.find_element_by_css_selector("#planner-view > div > nav.side.nopointer.ng-scope > header > button > div > span")
        new_2.click()

        time.sleep(3)

        numerical_box_sold_year_caprate_modal_spinner = self.driver.find_element_by_id("numerical_box_sold_year_caprate_modal-spinner")
        numerical_box_sold_year_caprate_modal_spinner.click()
        numerical_box_sold_year_caprate_modal_spinner.clear()

        if sold_year_caprate_1_list[3] == "0":
            sold_year_caprate_2 = sold_year_caprate_1_list[0]
            numerical_box_sold_year_caprate_modal_spinner.send_keys(sold_year_caprate_2)
            time.sleep(1)
            sold_year_caprate_3 = sold_year_caprate_1_list[1]
            numerical_box_sold_year_caprate_modal_spinner.send_keys(sold_year_caprate_3)
            time.sleep(1)
            sold_year_caprate_4 = sold_year_caprate_1_list[2]
            numerical_box_sold_year_caprate_modal_spinner.send_keys(sold_year_caprate_4)
            time.sleep(1)
        else:
            sold_year_caprate_2 =sold_year_caprate_1_list[0]
            numerical_box_sold_year_caprate_modal_spinner.send_keys(sold_year_caprate_2)
            time.sleep(1)
            sold_year_caprate_3 = sold_year_caprate_1_list[1]
            numerical_box_sold_year_caprate_modal_spinner.send_keys(sold_year_caprate_3)
            time.sleep(1)
            sold_year_caprate_4 = sold_year_caprate_1_list[2]
            numerical_box_sold_year_caprate_modal_spinner.send_keys(sold_year_caprate_4)
            time.sleep(1)
            sold_year_caprate_5 = sold_year_caprate_1_list[3]
            numerical_box_sold_year_caprate_modal_spinner.send_keys(sold_year_caprate_5)
            time.sleep(1)

        finish_4 = self.driver.find_element_by_css_selector("#planner-settings-modal > div > div.modal-footer > div > div.col-xs-4.text-center > button")
        finish_4.click()

        time.sleep(10)

    def assessment_result(self,y,bukken_data):
        self.y = y
        self.bukken_data = bukken_data
        
        printer_2 = self.driver.find_element_by_class_name("estimation-report-select-btn")
        printer_2.click()
        time.sleep(20)
        # Need to change coordinates
        pg.click(x=1300, y=500,clicks=1, interval=0, button="right")
        time.sleep(2)
        pg.click(x=1530, y=740,clicks=1, interval=0, button="left")
        time.sleep(10)
        pg.click(x=2100, y=750,clicks=1, interval=1, button="left")
        time.sleep(3)
        pg.click(x=1950, y=1300,clicks=1, interval=0, button="left")
        time.sleep(15)
        pg.click(x=2050, y=1400,clicks=1, interval=0, button="left")
        time.sleep(15)        
        
        name_of_building = self.bukken_data[self.y][7]
        kubun_report_name = "区分評価レポート_" + name_of_building + ".pdf"

        pyperclip.copy(kubun_report_name)
        pg.hotkey("ctrl", "v")
        time.sleep(5)
        pg.click(x=2400, y=1675,clicks=1, interval=0, button="left")
        time.sleep(20)
        
        handle_array_20 = driver.window_handles
        driver.switch_to.window(handle_array_20[2])

        time.sleep(7)

        printer = self.driver.find_element_by_class_name("print-btn")
        printer.click()

        time.sleep(20)
        pg.click(x=2050, y=1400,clicks=1, interval=0, button="left")
        time.sleep(10)
        main_report_name = name_of_building + "_gate.pdf"
        
        pyperclip.copy(main_report_name)
        pg.hotkey("ctrl", "v")
        time.sleep(3)
        pg.click(x=2400, y=1675,clicks=1, interval=0, button="left")
        time.sleep(5)