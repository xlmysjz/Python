#-*-coding:utf-8-*-
'''
Created on 2013-5-16

@author: Administrator
'''
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from urllib import urlopen

def draw():
    '''
    data=[(2007,8,113.2,114.2,112.2),
          (2007,9,112.8,115.8,109.8),
          (2007,10,111.0,116.0,106.0),
          (2007,11,109.8,116.8,102.8),
          (2007,12,107.3,115.3,99.3),
          (2008,1,105.2,114.2,96.2),
          (2008,2,104.1,114.1,94.1),
          (2008,3,99.9,110.9,88.9),
          (2008,4,94.8,106.8,82.8),
          (2008,5,91.2,104.2,78.2)]
          '''
    '''
    #�������pdf�ﻭһ�� hello word ������,
    d=Drawing(100,100)
    s=String(50,50,"hello word",textAnchor="middle")
    d.add(s)
    renderPDF.drawToFile(d,"hello.pdf","A simple PDF file")#renderPDF.drawToFile���ú������pdf�ļ��浽��ǰĿ¼��һ����hello.pdf���ļ���
    '''
    URL="http://www.swpc.noaa.gov/ftpdir/weekly/Predict.txt"#��364ҳ�������ַ��¼����̫�����ӵ�ȫ������
    COMMENT_CHARS="#:"
    drawing=Drawing(400,200)
    data=[]
    for line in urlopen(URL).readlines():
        #not isspace()���ж� ��һ�в�Ϊ���ַ�����not line[0] in COMMENT_CHARS��˵ ����ҳ��ȥ�� # �� . �Ĳ���
        if not line.isspace() and not line[0] in COMMENT_CHARS:
            data.append([float(n) for n in line.split()])
    #print data
    
    pred=[row[2] for row in data]
    high=[row[3] for row in data]
    low=[row[4] for row in data]
    times=[row[0]+row[1]/12.0 for row in data]
    
    lp=LinePlot()
    #���� x,y,height,width,�Լ�data
    lp.x=50 
    lp.y=50
    lp.height=125
    lp.width=300
    lp.data=[zip(times,pred),zip(times,high),zip(times,low)]
    lp.lines[0].strokeColor = colors.blue
    lp.lines[1].strokeColor = colors.red
    lp.lines[2].strokeColor = colors.green
    
    
    '''
    drawing.add(PolyLine(zip(times,pred),storkeColor=colors.blue))
    drawing.add(PolyLine(zip(times,high),storkeColor=colors.red))
    drawing.add(PolyLine(zip(times,low),storkeColor=colors.green))
    #drawing.add(PolyLine([(10,50),(100,50),(80,80)],storkeColor=colors.red))#�����ֱ�ӻ�һ����
    '''
    drawing.add(lp)
    drawing.add(String(250,150,"SunSpots",fontSize=14,fillColor=colors.red))
    
    renderPDF.drawToFile(drawing,"report.pdf","SunSpots")#renderPDF.drawToFile���ú������pdf�ļ��浽��ǰĿ¼��һ����report.pdf���ļ���
    
    #366


if __name__=="__main__":
    draw()
    print"��ִ����ϣ��뵽  ��Ŀ¼�²鿴 report.pdf"
    

