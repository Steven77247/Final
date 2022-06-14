#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import twstock

# get data
import pandas as pd
import pandas_datareader as pdr

# visual
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")
get_ipython().run_line_magic('matplotlib', 'inline')
import mpl_finance as mpf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# time
import datetime as datetime

# tkinter
import tkinter as tk


# In[4]:


def stock_candlestick_chart():
    
    #get the stock code and begin time
    code = int(block1.get().replace(' ', '').strip())
    y = int(block2.get().replace(' ', '').strip())
    m = int(block3.get().replace(' ', '').strip())
    d = int(block4.get().replace(' ', '').strip())
    
    #determine whether the company is 上市 or 上櫃
    if (f'{code}' in twstock.twse) == True:
        result = '\t' + '類股資訊: ' + "{}是上市公司".format(code) + '\t'          + '公司名稱:{}'.format(twstock.codes[f'{code}'].name)  + '\t'         + '上市日期:{}'.format(twstock.codes[f'{code}'].start) + '\t'         + '分類:{}'.format(twstock.codes[f'{code}'].group)
        Result['text'] = result
        techical_analysis(code)
        stock_twse(y,m,d,code)
    elif (f'{code}' in twstock.tpex) == True:
        result = '\t' + '類股資訊: ' + "{}是上櫃公司".format(code) + '\t'          + '公司名稱:{}'.format(twstock.codes[f'{code}'].name)  + '\t'         + '上市日期:{}'.format(twstock.codes[f'{code}'].start) + '\t'         + '分類:{}'.format(twstock.codes[f'{code}'].group)
        Result['text'] = result
        techical_analysis(code)
        stock_tpex(y,m,d,code)
    else:
        result = '找不到{}'.format(code) + '這間公司'
        Result['text'] = result
        


# In[5]:


def stock_twse(y,m,d,code):
    begin = datetime.datetime(y,m,d)
    stock = f'{code}.TW'
    df_twse = pdr.DataReader(stock, 'yahoo', start=begin)
    
    sma_5 = df_twse['Close'].rolling(5).mean()
    sma_10 = df_twse['Close'].rolling(10).mean()
    sma_20 = df_twse['Close'].rolling(20).mean()
    sma_60 = df_twse['Close'].rolling(60).mean()
    
    df_twse.index = df_twse.index.format(formatter=lambda x: x.strftime('%y-%m-%d')) 
  
    fig = plt.figure(figsize=(14, 6.5))

    ax = fig.add_axes([0.05,0.3,0.93,0.65])
    ax2 = fig.add_axes([0.05,0.1,0.93,0.2])
    
    if y == 2022 :  
        index_m = 10
    else:
        index_m = 20

    ax.set_xticks(range(0, len(df_twse.index), index_m))
    ax.set_xticklabels(df_twse.index[::index_m])
    mpf.candlestick2_ochl(ax, df_twse['Open'], df_twse['Close'], df_twse['High'],
                          df_twse['Low'], width=0.5, colorup='r', colordown='g', alpha=0.75)
    plt.rcParams['font.sans-serif']=['Microsoft JhengHei'] 
    ax.plot(df_twse.index,sma_5, '-' , color='orange' , label='5MA')
    ax.plot(df_twse.index,sma_10, '-' , color='blue' , label='10MA')
    ax.plot(df_twse.index,sma_20, '-' , color='red' , label='20MA')
    ax.plot(df_twse.index,sma_60, '-' , color='green' , label='60MA')

    plt.ylabel('成交量',size=20)

    mpf.volume_overlay(ax2, df_twse['Open'], df_twse['Close'], df_twse['Volume'],                        colorup='r', colordown='g', width=0.5, alpha=0.8)
    ax2.set_xticks(range(0, len(df_twse.index), index_m))
    ax2.set_xticklabels(df_twse.index[::index_m])

    ax.legend(fontsize=15)
    ax.grid()
    ax2.grid()
    plt.show()
        
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(side = 'bottom', fill = 'both', padx = 15, pady = 5)

    


# In[6]:


def stock_tpex(y,m,d,code):
    begin = datetime.datetime(y,m,d)
    stock = f'{code}.TWO'
    df_tpex = pdr.DataReader(stock, 'yahoo', start=begin)
    
    sma_5 = df_tpex['Close'].rolling(5).mean()
    sma_10 = df_tpex['Close'].rolling(10).mean()
    sma_20 = df_tpex['Close'].rolling(20).mean()
    sma_60 = df_tpex['Close'].rolling(60).mean()
    
    df_tpex.index = df_tpex.index.format(formatter=lambda x: x.strftime('%y-%m-%d')) 

    fig = plt.figure(figsize=(14, 6.5))

    ax = fig.add_axes([0.05,0.3,0.93,0.65])
    ax2 = fig.add_axes([0.05,0.1,0.93,0.2])
    
    if y == 2022 :  
        index_m = 15
    else:
        index_m = 20

    ax.set_xticks(range(0, len(df_tpex.index), index_m))
    ax.set_xticklabels(df_tpex.index[::index_m])
    mpf.candlestick2_ochl(ax, df_tpex['Open'], df_tpex['Close'], df_tpex['High'],
                          df_tpex['Low'], width=0.6, colorup='r', colordown='g', alpha=0.75)
    plt.rcParams['font.sans-serif']=['Microsoft JhengHei'] 
    ax.plot(df_tpex.index,sma_5, '-' , color='orange' , label='5MA')
    ax.plot(df_tpex.index,sma_10, '-' , color='blue' , label='10MA')
    ax.plot(df_tpex.index,sma_20, '-' , color='red' , label='20MA')
    ax.plot(df_tpex.index,sma_60, '-' , color='green' , label='60MA')

    plt.ylabel('成交量',size=20)

    mpf.volume_overlay(ax2, df_tpex['Open'], df_tpex['Close'], df_tpex['Volume'],                        colorup='r', colordown='g', width=0.5, alpha=0.8)
    ax2.set_xticks(range(0, len(df_tpex.index), index_m))
    ax2.set_xticklabels(df_tpex.index[::index_m])

    ax.legend(fontsize=15)
    ax.grid()
    ax2.grid()
    plt.show()
    
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(side = 'bottom', fill = 'both', padx = 15, pady = 5)
    


# In[7]:


#Technical Analysis
def techical_analysis(code):
    stock_code = str(code)
    stock_analysis = twstock.Stock(stock_code)
    
    now_price = sum(stock_analysis.price[-1:])
    stock_analysis_5 = stock_analysis.price[-5:]
    stock_analysis_10 = stock_analysis.price[-10:]
    stock_analysis_20 = stock_analysis.price[-20:]
    stock_analysis_60 = stock_analysis.price[-60:]
    
    #先判斷今天收盤價(or目前價格)在五日線之上或之下
    if now_price > sum(stock_analysis_5)/len(stock_analysis_5):
        if now_price > sum(stock_analysis_10)/len(stock_analysis_10):
            if now_price > sum(stock_analysis_20)/len(stock_analysis_20):
                if now_price > sum(stock_analysis_60)/len(stock_analysis_60):
                    if now_price > max(stock_analysis_60):
                        Technical['text'] = '技術分析:現在均線為多頭排列，可以沿著五日線去操作。僅需留意成交量為爆大量時即可。'
                    else:
                        Technical['text'] = '技術分析:現在均線為多頭排列，但有前高{}的壓力，除了遇壓力關前須留意外可沿著五日線去操作。'.format(max(stock_analysis_60))
                else:
                    Technical['text'] = '技術分析:上有季線{}作為壓力線。過了壓力可能為大多頭，否則遇壓力須多加留意。'.format(sum(stock_analysis_60)/len(stock_analysis_60))
            else:
                Technical['text'] = '技術分析:上有月線{}作為壓力線，遇壓力須多加留意。'.format(sum(stock_analysis_20)/len(stock_analysis_20))
        else:
            Technical['text'] = '技術分析:上有十日線{}作為壓力線，遇壓力須多加留意。'.format(sum(stock_analysis_10)/len(stock_analysis_10))
    elif now_price < sum(stock_analysis_5)/len(stock_analysis_5):
        if now_price < sum(stock_analysis_10)/len(stock_analysis_10):
            if now_price < sum(stock_analysis_20)/len(stock_analysis_20):
                if now_price < sum(stock_analysis_60)/len(stock_analysis_60):
                    if now_price < min(stock_analysis_60):
                        Technical['text'] = '技術分析:現在均線為空頭排列，可做空或觀察何時成交量為爆大量時即可。'
                    else:
                        Technical['text'] = '技術分析:現在均線為空頭排列。若遇到前低{}的支撐，手上若持有則須非常留意。'.format(min(stock_analysis_60))
                else:
                    Technical['text'] ='技術分析:下有季線{}作為支撐線。若遇到季線支撐，則可依情況減少持股比例或全出。'.format(sum(stock_analysis_60)/len(stock_analysis_60))
            else:
                Technical['text'] = '技術分析:下有月線{}作為支撐線，若遇到月線支撐，則可依情況減少持股比例。'.format(sum(stock_analysis_20)/len(stock_analysis_20))
        else:
            Technical['text'] = '技術分析:下有十日線{}作為支撐線，若沒有低於支撐的話還可以續抱。'.format(sum(stock_analysis_10)/len(stock_analysis_10))
        


# In[8]:


#initializaiton
win = tk.Tk()
win.title('股市K線圖查詢系統')
win.geometry('1400x750') #width x height

def validate(P):
    #print(P)
    if str.isdigit(P) or P == '':
        return True
    else:
        return False
    
vcmd = (win.register(validate), '%P')

#輸入股票代號
frame1 = tk.Frame(win)
frame1.place(x=0,y=0)
start_station = tk.Label(frame1, text='請輸入股票代號 :', font=('microsoft yahei', 16))
start_station.grid(row=0,column=0,padx=10,pady=10)
block1 = tk.Entry(frame1, width=20, font=('microsoft yahei', 16),                   validatecommand=vcmd, takefocus=1)
block1.grid(row=0,column=1,padx=5,pady=20)

#輸入起始日期
#年
frame2 = tk.Frame(win)
frame2.place(x=0,y=60)
year = tk.Label(frame2, text='請輸入日期  輸入年 :', font=('microsoft yahei', 14))
year.grid(row=1,column=0,padx=10,pady=10)
block2 = tk.Entry(frame2, width=10, font=('microsoft yahei', 14),                    validatecommand=vcmd, takefocus=1)
block2.grid(row=1,column=2,padx=5,pady=10)

#月
frame3 = tk.Frame(win)
frame3.place(x=325,y=60)
month = tk.Label(frame3, text='輸入月 :', font=('microsoft yahei', 14))
month.grid(row=1,column=3,padx=10,pady=10)
block3 = tk.Entry(frame3, width=10, font=('microsoft yahei', 14),                    validatecommand=vcmd, takefocus=1)
block3.grid(row=1,column=4,padx=5,pady=10)

#日
frame4 = tk.Frame(win)
frame4.place(x=550,y=60)
day = tk.Label(frame4, text='輸入日 :', font=('microsoft yahei', 14))
day.grid(row=1,column=5,padx=10,pady=10)
block4 = tk.Entry(frame4, width=10, font=('microsoft yahei', 14),                    validatecommand=vcmd, takefocus=1)
block4.grid(row=1,column=6,padx=5,pady=10)


#按鈕設置
frame5 = tk.Frame(win)
frame5.place(x=0,y=120)
button = tk.Button(frame5, text='Search', font=('microsoft yahei', 16),                    width=30, height=1, command=stock_candlestick_chart)
button.grid(row=2,column=0,padx=10,pady=5)


#show the candlestick chart
frame6 = tk.Frame(win)
frame6.place(x=0,y=180)
Result = tk.Label(frame6, text=" ", font=('Arial', 12) , justify= tk.LEFT)
Technical = tk.Label(frame6, text="", font=('Arial', 12) , justify= tk.LEFT)
Result.grid(row=4,column=0,padx=10,pady=10)
Technical.grid(row=6,column=0,padx=10,pady=10)


win.mainloop()


# In[ ]:




