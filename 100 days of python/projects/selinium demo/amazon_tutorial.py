from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get(
    "https://www.amazon.in/Vans-Sk8-Hi-Unisex-Casual-High-Top/dp/B07LBDKLG3/?_encoding=UTF8&pd_rd_w=Zinh2&content-id=amzn1.sym.b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_p=b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_r=JYD1CSCVEGV6PBPGJ54C&pd_rd_wg=2LBTY&pd_rd_r=e2fb2563-d719-4b30-9cba-7a703f03081f&ref_=pd_gw_ci_mcx_mr_hp_atf_m"
)

# You can always find a element using xpath
# inspect the element and right click on it to copy the xpath of that element
price = driver.find_element(
    by=By.XPATH,
    value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/span[2]/span[2]',
)


print(price.text)
