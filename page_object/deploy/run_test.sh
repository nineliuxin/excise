# export PRO_PATH

cd $PRO_PATH/data

if [[ "${os_type}" == "Darwin" ]]; then
	sed -i "" "s/device_ip/${device_ip}/g" driver.yml
else
  sed -i "s/device_ip/${device_ip}/g" driver.yml
fi


cd $PRO_PATH/testcases
pytest -v test_login.py --alluredir ../allure_results
allure serve ../allure_results