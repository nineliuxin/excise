
    node('new'){
        stage("同步源码"){
            git([url:'https://github.com/nineliuxin/excise.git',credentialsId:'2e749226-84a2-418a-aadd-104500ed68a3',branch:'master'])
        }
        stage("运行测试代码"){
            sh '''
                . ~/.bash_profile
                . /etc/profile
                cd page_object
                export PRO_PATH=`pwd`
                export os_type=`uname`
                cd data
                if [[ "${os_type}" == "Darwin" ]]; then
                    sed -i "" "s/device_ip/${device_ip}/g" driver.yaml
                else
                    sed -i "s/device_ip/${device_ip}/g" driver.yaml
                fi
                cd $PRO_PATH/testcases
                ~/.pyenv/shims/pytest -v test_login.py --alluredir ../allure_results
                allure serve ../allure_results
            '''
        }
    }
