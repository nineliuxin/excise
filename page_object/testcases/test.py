from selenium.webdriver.common.by import By

b = (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
print(type(b))
print(*b)

c = {"name": "liuxin", "age": 12}
print(type(c))
print(type(*c))