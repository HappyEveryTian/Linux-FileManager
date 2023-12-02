#!/bin/bash

# 更新yum源
yum upgrade -y

# 安装python3
yum install python3

# 安装python3扩展
yum install python3-devel

# 安装psutil
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple psutil==5.5.1
if [ $? -ne 0 ]; then
    pip3 install psutil==5.5.1
    if [ $? -ne 0 ]; then
        echo "安装psutil失败，请检查错误信息。"
        exit 1
    fi
fi

# 安装PyQt5
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple PyQt5==5.12
if [ $? -ne 0 ]; then
    pip3 install PyQt5==5.12
    if [ $? -ne 0 ]; then
        echo "安装PyQt5失败，请检查错误信息。"
        exit 1
    fi
fi

# 安装PyQt5-sip
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple PyQt5-sip==4.19.14
if [ $? -ne 0 ]; then
    pip3 install PyQt5-sip==4.19.14
    if [ $? -ne 0 ]; then
        echo "安装PyQt5-sip失败，请检查错误信息。"
        exit 1
    fi
fi

# 安装python-dateutil
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple python-dateutil==2.8.0
if [ $? -ne 0 ]; then
    pip3 install python-dateutil==2.8.0
    if [ $? -ne 0 ]; then
        echo "安装python-dateutil失败，请检查错误信息。"
        exit 1
    fi
fi

# 安装pytz
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pytz==2018.9
if [ $? -ne 0 ]; then
    pip3 install pytz==2018.9
    if [ $? -ne 0 ]; then
        echo "安装pytz失败，请检查错误信息。"
        exit 1
    fi
fi

# 安装six
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple six==1.12.0
if [ $? -ne 0 ]; then
    pip3 install six==1.12.0
    if [ $? -ne 0 ]; then
        echo "安装six失败，请检查错误信息。"
        exit 1
    fi
fi

# 安装chardet
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple chardet==5.0.0
if [ $? -ne 0 ]; then
    pip3 install chardet==5.0.0
    if [ $? -ne 0 ]; then
        echo "安装chardet失败，请检查错误信息。"
        exit 1
    fi
fi

echo "所有包已成功安装!。"
