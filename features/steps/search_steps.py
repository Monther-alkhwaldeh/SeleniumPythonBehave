import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I navigate to google.com')
def step_impl(context):
    context.driver.get('https://google.com')
    context.driver.implicitly_wait(10)


@when(u'I validate the page title')
def step_impl(context):
    print(u'STEP: When I validate the page title')
    title = context.driver.title
    print("Title is " + title)
    assert "Googles" in title


@then(u'I Enter the text as "{search_text}"')
def step_impl(context, search_text):
    print(u'STEP: Then I Enter the text as Hello Seleinum')
    context.driver.find_element(By.NAME, 'q').send_keys(search_text)
    time.sleep(2)


@then(u'I Click The search button')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[4]/div[6]/center/input[1]').click()
    time.sleep(2)