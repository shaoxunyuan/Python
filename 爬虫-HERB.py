# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:27:28 2024

@author: ysx0226
"""

from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.edge.service import Service  
from selenium.webdriver.edge.options import Options  
import os  
import time  
import glob  
import re
import random  
from datetime import datetime  
download_dir = r"C:/Users/ysx0226/Downloads"    ### 根据自己的电脑修改


edge_driver_path = 'D:/OneDrive/Script_Python/msedgedriver.exe'  
edge_options = Options()   
service = Service(executable_path=edge_driver_path)  
driver = webdriver.Edge()

herbID = "HERB001779"  # 输入 ID，更改为需要的中药名字
url = f'http://herb.ac.cn/Detail/?v={herbID}&label=Herb'  
driver.get(url)  

time.sleep(random.randint(15, 25)) 

download_button = driver.find_element(By.XPATH, "(//button[span[text()='Download']])[1]")  
download_button.click()

time.sleep(random.randint(15, 25)) 

download_button = driver.find_element(By.XPATH, "(//button[span[text()='Download']])[2]")    
download_button.click()  # 点击下载按钮

time.sleep(random.randint(15, 25)) 

download_button = driver.find_element(By.XPATH, "(//button[span[text()='Download']])[3]")    
download_button.click()  # 点击下载按钮


current_date = datetime.now().strftime("%Y_%m_%d")  

# 定义已知的文件名  
original_files = [  
    f"herb_ingredient{current_date}.xlsx",  
    f"drug_paper_target{current_date}.xlsx",  
    f"herb_disease{current_date}.xlsx"  
]  

# 新文件名模板  
new_names = [  
    f"{herbID}_ingredient.xlsx",  
    f"{herbID}_target.xlsx",  
    f"{herbID}_disease.xlsx"  
]  

# 重命名每个文件  
for original, new in zip(original_files, new_names):  
    original_file_path = os.path.join(download_dir, original)  
    new_file_path = os.path.join(download_dir, new)  

    # 检查原始文件是否存在并进行重命名  
    if os.path.exists(original_file_path):  
        os.rename(original_file_path, new_file_path)  
        print(f"文件 {original} 已重命名为 {new}")  
    else:  
        print(f"未找到文件: {original_file_path}")  