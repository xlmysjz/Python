#-*-coding:utf-8-*-
#!/usr/bin/env python

'''
ѡ��manage.py-�Ҽ��C Run As �C Run Configurations 
�������в���  (x) = Argumentsѡ�
runserver --noreload
֮�󣬾Ϳ�����eclipseֱ����������
ѡ��manage.py���Ҽ� Python Run
��ʾ����� ��֤��������
Validating models...

0 errors found
May 30, 2013 - 17:25:44
Django version 1.5.1, using settings 'PythonDjangoPro.settings'
Development server is running at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[30/May/2013 17:25:47] "GET / HTTP/1.1" 200 1966

'''

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PythonDjangoPro.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
