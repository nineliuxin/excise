
    node('$node'){
        stage("同步源码"){
            git([url:'https://github.com/nineliuxin/excise.git',branch:'${branch}'])
        }
        stage("运行测试代码"){
            sh '''
                . ~/bash_profile
                cd page_object
                export PRO_PATH=`pwd`
                export os_type=`uname`
                cd data
                if [[ "${os_type}" == "Darwin" ]]; then
                    sed -i "" "s/device_ip/${device_ip}/g" driver.yml
                else
                    sed -i "s/device_ip/${device_ip}/g" driver.yml
                fi
                cd $PRO_PATH/testcases
                pytest -v test_login.py --alluredir ../allure_results
                allure serve ../allure_results
            '''
        }
    }
