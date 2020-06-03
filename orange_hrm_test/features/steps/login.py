from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@given("user navigate to orange hrm website")
def step_impl(context):
    context.browser.get("https://opensource-demo.orangehrmlive.com/")


@when("user enter username")
def step_impl(context):
    context.browser.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys("admin")


@step("user enter password")
def step_impl(context):
    context.browser.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys("admin123")


@then("user click on login button")
def step_impl(context):
    context.browser.find_element(By.XPATH, "//input[@id='btnLogin']").click()


@step("user click on menu leave Module")
def step_impl(context):
    action_chains = ActionChains(context.browser)
    action_chains.move_to_element(
        context.browser.find_element(By.XPATH, "//a[@id='menu_leave_viewLeaveModule']")).perform()
    action_chains.move_to_element(context.browser.find_element(By.XPATH, "//a[@id='menu_leave_Reports']")).perform()
    context.browser.find_element(By.ID, "menu_leave_viewLeaveBalanceReport").click()


@then("user see leave balance report page")
def step_impl(context):
    select = Select(context.browser.find_element_by_id('leave_balance_report_type'))
    select.select_by_visible_text("Employee")

    context.browser.find_element_by_id("leave_balance_employee_empName").send_keys("Rahul")
    context.browser.find_element_by_id("viewBtn").click()


@step("user logout form website")
def step_impl(context):
    context.browser.find_element(By.XPATH, "//a[@id='welcome']").click()
    context.browser.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()
