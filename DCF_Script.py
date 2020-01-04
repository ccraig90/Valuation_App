import statsmodels.formula.api as sm
from datetime import datetime
import numpy as np
import pandas as pd
import datetime as dt
from IPython.display import display
from collections import OrderedDict
import timeit
from dateutil import relativedelta
from datetime import date, timedelta

IS = pd.read_excel(io = '/Users/Chad/Desktop/BWXT IS.xlsx')
IS.set_index('Quarter',inplace = True)
IS = IS.transpose()
IS['Q#'] = IS.index.str[:2]

def IS_Forecast(Income_Statement):
IS = Income_Statement
# IS = Income_Statement
Forecast_list = ['Revenue','Cost of Revenue','Operating Expenses',
            'Selling, General & Admin','Research & Development','Other Operating Expense',
                'Net Income Avail to Common, GAAP','Operating Income (Loss)']
i = 1
revenue_c = 0
percent_COGS_list= []
percent_Op_Exp_list = []
percent_SGA_list = []
percent_R_and_D_list = []
percent_Net_Income_list = []

while i < len(IS[Forecast_list[0]]):

    """ Revenue Change Quarter over Quarter Average"""
    revenue_change = ((IS[Forecast_list[0]][i] - IS[Forecast_list[0]][i-1])/IS[Forecast_list[0]][i-1])
    revenue_c += revenue_change
    revenue_change = revenue_change/len(IS[Forecast_list[0]])

    """ Percent of COGS average for each quarter"""
    percent_COGS = IS[Forecast_list[1]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_COGS
    percent_COGS_list.append(percent_COGS) #add each percent COGS to a list

    """Percent of Operating Expense"""
    percent_Op_Exp = IS[Forecast_list[2]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_Op_Exp
    percent_Op_Exp_list.append(percent_Op_Exp) #add each percent_Op_Exp to a list

    """Percent of SGA"""
    percent_SGA = IS[Forecast_list[3]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_Op_Exp
    percent_SGA_list.append(percent_SGA) #add each percent_Op_Exp to a list

    """Percent R and D"""
    percent_R_and_D = IS[Forecast_list[4]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_Op_Exp
    percent_R_and_D_list.append(percent_R_and_D) #add each percent_Op_Exp to a list
    
    """Percent Net Income"""
    percent_Net_Income = IS[Forecast_list[6]][i-1]/IS[Forecast_list[7]][i-1]
    percent_Net_Income_list.append(percent_Net_Income)
    i += 1
    
percent_COGS_list =[item for item in percent_COGS_list if str(item) != 'nan'] #remove nan values from percent_C list
percent_COGS = sum(percent_COGS_list)/len(percent_COGS_list) #average COGS percent

percent_Op_Exp_list = [item for item in percent_Op_Exp_list if str(item) != 'nan']#remove nan values from percent_Op_Exp list
percent_Op_Exp = sum(percent_Op_Exp_list)/len(percent_Op_Exp_list) #quarter average OP_Exp

percent_SGA_list = [item for item in percent_SGA_list if str(item) != 'nan']
percent_SGA = sum(percent_SGA_list)/len(percent_SGA_list)

percent_R_and_D_list = [item for item in percent_R_and_D_list if str(item) != 'nan']
percent_R_and_D = sum(percent_R_and_D_list)/len(percent_R_and_D_list)

percent_Net_Income_list = [item for item in percent_Net_Income_list if str(item) != 'nan']
percent_Net_Income = sum(percent_Net_Income_list)/len(percent_Net_Income_list)


Overall_averages = {'Revenue Change':revenue_change,
                    'Percent_COGS':percent_COGS,
                    'Percent Op Exp':percent_Op_Exp,
                    'Percent SGA':percent_SGA,
                    'Percent RandD':percent_R_and_D,
                    'Percent Net Income':percent_Net_Income}
"""
Quarter 1
"""
IS = Income_Statement
IS = IS[(IS['Q#'] == 'Q1')]
i = 1
revenue_c = 0
percent_COGS_list= []
percent_Op_Exp_list = []
percent_SGA_list = []
percent_R_and_D_list = []


while i < len(IS[Forecast_list[0]]):

    """ Revenue Change Quarter over Quarter Average"""
    revenue_change = ((IS[Forecast_list[0]][i] - IS[Forecast_list[0]][i-1])/IS[Forecast_list[0]][i-1])
    revenue_c += revenue_change
    revenue_change = revenue_change/len(IS[Forecast_list[0]])

    """ Percent of COGS average for each quarter"""
    percent_COGS = IS[Forecast_list[1]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_COGS
    percent_COGS_list.append(percent_COGS) #add each percent COGS to a list

    """Percent of Operating Expense"""
    percent_Op_Exp = IS[Forecast_list[2]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_Op_Exp
    percent_Op_Exp_list.append(percent_Op_Exp) #add each percent_Op_Exp to a list

    """Percent of SGA"""
    percent_SGA = IS[Forecast_list[3]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_Op_Exp
    percent_SGA_list.append(percent_SGA) #add each percent_Op_Exp to a list

    """Percent R and D"""
    percent_R_and_D = IS[Forecast_list[4]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_Op_Exp
    percent_R_and_D_list.append(percent_R_and_D) #add each percent_Op_Exp to a list
    
    """Percent Net Income"""
    percent_Net_Income = IS[Forecast_list[6]][i-1]/IS[Forecast_list[7]][i-1]
    percent_Net_Income_list.append(percent_Net_Income)
    

    i += 1
percent_COGS_list =[item for item in percent_COGS_list if str(item) != 'nan'] #remove nan values from percent_C list
percent_COGS = sum(percent_COGS_list)/len(percent_COGS_list) #average COGS percent

percent_Op_Exp_list = [item for item in percent_Op_Exp_list if str(item) != 'nan']#remove nan values from percent_Op_Exp list
percent_Op_Exp = sum(percent_Op_Exp_list)/len(percent_Op_Exp_list) #quarter average OP_Exp

percent_SGA_list = [item for item in percent_SGA_list if str(item) != 'nan']
percent_SGA = sum(percent_SGA_list)/len(percent_SGA_list)

percent_R_and_D_list = [item for item in percent_R_and_D_list if str(item) != 'nan']
percent_R_and_D = sum(percent_R_and_D_list)/len(percent_R_and_D_list)

percent_Net_Income_list = [item for item in percent_Net_Income_list if str(item) != 'nan']
percent_Net_Income = sum(percent_Net_Income_list)/len(percent_Net_Income_list)

Q1_averages = {'Revenue Change':revenue_change,
                    'Percent_COGS':percent_COGS,
                    'Percent Op Exp':percent_Op_Exp,
                    'Percent SGA':percent_SGA,
                    'Percent RandD':percent_R_and_D,
                    'Percent Net Income':percent_Net_Income}
"""
Quarter 2
"""
IS = Income_Statement
IS = IS[(IS['Q#'] == 'Q2')]
i = 1
revenue_c = 0
percent_COGS_list= []
percent_Op_Exp_list = []
percent_SGA_list = []
percent_R_and_D_list = []

while i < len(IS[Forecast_list[0]]):

    """ Revenue Change Quarter over Quarter Average"""
    revenue_change = ((IS[Forecast_list[0]][i] - IS[Forecast_list[0]][i-1])/IS[Forecast_list[0]][i-1])
    revenue_c += revenue_change
    revenue_change = revenue_change/len(IS[Forecast_list[0]])

    """ Percent of COGS average for each quarter"""
    percent_COGS = IS[Forecast_list[1]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_COGS
    percent_COGS_list.append(percent_COGS) #add each percent COGS to a list

    """Percent of Operating Expense"""
    percent_Op_Exp = IS[Forecast_list[2]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_Op_Exp
    percent_Op_Exp_list.append(percent_Op_Exp) #add each percent_Op_Exp to a list

    """Percent of SGA"""
    percent_SGA = IS[Forecast_list[3]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_Op_Exp
    percent_SGA_list.append(percent_SGA) #add each percent_Op_Exp to a list

    """Percent R and D"""
    percent_R_and_D = IS[Forecast_list[4]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_Op_Exp
    percent_R_and_D_list.append(percent_R_and_D) #add each percent_Op_Exp to a list
    
    """Percent Net Income"""
    percent_Net_Income = IS[Forecast_list[6]][i-1]/IS[Forecast_list[7]][i-1]
    percent_Net_Income_list.append(percent_Net_Income)

    
    i += 1
    
percent_COGS_list =[item for item in percent_COGS_list if str(item) != 'nan'] #remove nan values from percent_C list
percent_COGS = sum(percent_COGS_list)/len(percent_COGS_list) #average COGS percent

percent_Op_Exp_list = [item for item in percent_Op_Exp_list if str(item) != 'nan']#remove nan values from percent_Op_Exp list
percent_Op_Exp = sum(percent_Op_Exp_list)/len(percent_Op_Exp_list) #quarter average OP_Exp

percent_SGA_list = [item for item in percent_SGA_list if str(item) != 'nan']
percent_SGA = sum(percent_SGA_list)/len(percent_SGA_list)

percent_R_and_D_list = [item for item in percent_R_and_D_list if str(item) != 'nan']
percent_R_and_D = sum(percent_R_and_D_list)/len(percent_R_and_D_list)

percent_Net_Income_list = [item for item in percent_Net_Income_list if str(item) != 'nan']
percent_Net_Income = sum(percent_Net_Income_list)/len(percent_Net_Income_list)



Q2_averages = {'Revenue Change':revenue_change,
                    'Percent_COGS':percent_COGS,
                    'Percent Op Exp':percent_Op_Exp,
                    'Percent SGA':percent_SGA,
                    'Percent RandD':percent_R_and_D,
                    'Percent Net Income':percent_Net_Income}
"""
Quarter 3
"""
IS = Income_Statement
IS = IS[(IS['Q#'] == 'Q3')]
i = 1
revenue_c = 0
percent_COGS_list= []
percent_Op_Exp_list = []
percent_SGA_list = []
percent_R_and_D_list = []

while i < len(IS[Forecast_list[0]]):

    """ Revenue Change Quarter over Quarter Average """
    revenue_change = ((IS[Forecast_list[0]][i] - IS[Forecast_list[0]][i-1])/IS[Forecast_list[0]][i-1])
    revenue_c += revenue_change
    revenue_change = revenue_change/len(IS[Forecast_list[0]])

    """ Percent of COGS average for each quarter """
    percent_COGS = IS[Forecast_list[1]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_COGS
    percent_COGS_list.append(percent_COGS) #add each percent COGS to a list

    """ Percent of Operating Expense """
    percent_Op_Exp = IS[Forecast_list[2]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_Op_Exp
    percent_Op_Exp_list.append(percent_Op_Exp) #add each percent_Op_Exp to a list

    """ Percent of SGA """
    percent_SGA = IS[Forecast_list[3]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_Op_Exp
    percent_SGA_list.append(percent_SGA) #add each percent_Op_Exp to a list

    """ Percent R and D """
    percent_R_and_D = IS[Forecast_list[4]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_Op_Exp
    percent_R_and_D_list.append(percent_R_and_D) #add each percent_Op_Exp to a list
    
    """Percent Net Income"""
    percent_Net_Income = IS[Forecast_list[6]][i-1]/IS[Forecast_list[7]][i-1]
    percent_Net_Income_list.append(percent_Net_Income)

    
    i += 1
percent_COGS_list =[item for item in percent_COGS_list if str(item) != 'nan'] #remove nan values from percent_C list
percent_COGS = sum(percent_COGS_list)/len(percent_COGS_list) #average COGS percent

percent_Op_Exp_list = [item for item in percent_Op_Exp_list if str(item) != 'nan']#remove nan values from percent_Op_Exp list
percent_Op_Exp = sum(percent_Op_Exp_list)/len(percent_Op_Exp_list) #quarter average OP_Exp

percent_SGA_list = [item for item in percent_SGA_list if str(item) != 'nan']
percent_SGA = sum(percent_SGA_list)/len(percent_SGA_list)

percent_R_and_D_list = [item for item in percent_R_and_D_list if str(item) != 'nan']
percent_R_and_D = sum(percent_R_and_D_list)/len(percent_R_and_D_list)

percent_Net_Income_list = [item for item in percent_Net_Income_list if str(item) != 'nan']
percent_Net_Income = sum(percent_Net_Income_list)/len(percent_Net_Income_list)


Q3_averages = {'Revenue Change':revenue_change,
                    'Percent_COGS':percent_COGS,
                    'Percent Op Exp':percent_Op_Exp,
                    'Percent SGA':percent_SGA,
                    'Percent RandD':percent_R_and_D,
                    'Percent Net Income':percent_Net_Income}
"""
Quarter 4
"""
IS = Income_Statement
IS = IS[(IS['Q#'] == 'Q4')]
i = 1
revenue_c = 0
percent_COGS_list= []
percent_Op_Exp_list = []
percent_SGA_list = []
percent_R_and_D_list = []

while i < len(IS[Forecast_list[0]]):

    """ Revenue Change Quarter over Quarter Average """
    revenue_change = ((IS[Forecast_list[0]][i] - IS[Forecast_list[0]][i-1])/IS[Forecast_list[0]][i-1])
    revenue_c += revenue_change
    revenue_change = revenue_change/len(IS[Forecast_list[0]])

    """ Percent of COGS average for each quarter """
    percent_COGS = IS[Forecast_list[1]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_COGS
    percent_COGS_list.append(percent_COGS) #add each percent COGS to a list

    """ Percent of Operating Expense """
    percent_Op_Exp = IS[Forecast_list[2]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_Op_Exp
    percent_Op_Exp_list.append(percent_Op_Exp) #add each percent_Op_Exp to a list

    """ Percent of SGA """
    percent_SGA = IS[Forecast_list[3]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_Op_Exp
    percent_SGA_list.append(percent_SGA) #add each percent_Op_Exp to a list

    """ Percent R and D """
    percent_R_and_D = IS[Forecast_list[4]][i-1]/IS[Forecast_list[0]][i-1] #itterate through to find percent_Op_Exp
    percent_R_and_D_list.append(percent_R_and_D) #add each percent_Op_Exp to a list
    
    """Percent Net Income"""
    percent_Net_Income = IS[Forecast_list[6]][i-1]/IS[Forecast_list[7]][i-1]
    percent_Net_Income_list.append(percent_Net_Income)
    
    i += 1
    
percent_COGS_list =[item for item in percent_COGS_list if str(item) != 'nan'] #remove nan values from percent_C list
percent_COGS = sum(percent_COGS_list)/len(percent_COGS_list) #average COGS percent

percent_Op_Exp_list = [item for item in percent_Op_Exp_list if str(item) != 'nan']#remove nan values from percent_Op_Exp list
percent_Op_Exp = sum(percent_Op_Exp_list)/len(percent_Op_Exp_list) #quarter average OP_Exp

percent_SGA_list = [item for item in percent_SGA_list if str(item) != 'nan']
percent_SGA = sum(percent_SGA_list)/len(percent_SGA_list)

percent_R_and_D_list = [item for item in percent_R_and_D_list if str(item) != 'nan']
percent_R_and_D = sum(percent_R_and_D_list)/len(percent_R_and_D_list)

percent_Net_Income_list = [item for item in percent_Net_Income_list if str(item) != 'nan']
percent_Net_Income = sum(percent_Net_Income_list)/len(percent_Net_Income_list)


Q4_averages = {'Revenue Change':revenue_change,
                    'Percent_COGS':percent_COGS,
                    'Percent Op Exp':percent_Op_Exp,
                    'Percent SGA':percent_SGA,
                    'Percent RandD':percent_R_and_D,
                    'Percent Net Income':percent_Net_Income}

return Overall_averages,Q1_averages,Q2_averages,Q3_averages,Q4_averages

def Estimated_Forecast(IS_forecast,IS):

Revenue_last = IS['Revenue'][-3]
Quarter_last = IS['Q#'][-3]
Percent_change = []
Forecasted_revenue = []
Forecasted_COGS = []
Forecasted_Op_Exp = []
Forecasted_SGA = []
Forecasted_RandD = []
Forecasted_Gross_Revenue = []
Forecasted_Op_Income = []
Forecasted_Net_Income = []

if Quarter_last == 'Q1':
    Percent_change = [IS_forecast[2]['Revenue Change'], IS_forecast[3]['Revenue Change'], IS_forecast[4]['Revenue Change'], IS_forecast[1]['Revenue Change']]
    Percent_COGS = [IS_forecast[2]['Percent_COGS'], IS_forecast[3]['Percent_COGS'], IS_forecast[4]['Percent_COGS'],IS_forecast[1]['Percent_COGS']]
    Percent_Op_Exp = [IS_forecast[2]['Percent Op Exp'], IS_forecast[3]['Percent Op Exp'], IS_forecast[4]['Percent Op Exp'],IS_forecast[1]['Percent Op Exp']]
    Percent_SGA = [IS_forecast[2]['Percent SGA'], IS_forecast[3]['Percent SGA'], IS_forecast[4]['Percent SGA'],IS_forecast[1]['Percent SGA']]
    Percent_RandD = [IS_forecast[2]['Percent RandD'], IS_forecast[3]['Percent RandD'], IS_forecast[4]['Percent RandD'], IS_forecast[1]['Percent RandD']]
    Percent_Net_Income = [IS_forecast[2]['Percent Net Income'], IS_forecast[3]['Percent Net Income'], IS_forecast[4]['Percent Net Income'], IS_forecast[1]['Percent Net Income']]
    
elif Quarter_last == 'Q2':
    Percent_change = [IS_forecast[3]['Revenue Change'], IS_forecast[4]['Revenue Change'], IS_forecast[1]['Revenue Change'], IS_forecast[2]['Revenue Change']]
    Percent_COGS = [IS_forecast[3]['Percent_COGS'], IS_forecast[4]['Percent_COGS'], IS_forecast[1]['Percent_COGS'],IS_forecast[2]['Percent_COGS']]
    Percent_Op_Exp = [IS_forecast[3]['Percent Op Exp'], IS_forecast[4]['Percent Op Exp'], IS_forecast[1]['Percent Op Exp'],IS_forecast[2]['Percent Op Exp']]
    Percent_SGA = [IS_forecast[3]['Percent SGA'], IS_forecast[4]['Percent SGA'], IS_forecast[1]['Percent SGA'],IS_forecast[2]['Percent SGA']]
    Percent_RandD = [IS_forecast[3]['Percent RandD'], IS_forecast[4]['Percent RandD'], IS_forecast[1]['Percent RandD'], IS_forecast[2]['Percent RandD']]
    Percent_Net_Income = [IS_forecast[3]['Percent Net Income'], IS_forecast[4]['Percent Net Income'], IS_forecast[1]['Percent Net Income'], IS_forecast[2]['Percent Net Income']]
elif Quarter_last == 'Q3':
    Percent_change = [IS_forecast[4]['Revenue Change'], IS_forecast[1]['Revenue Change'], IS_forecast[2]['Revenue Change'], IS_forecast[3]['Revenue Change']]
    Percent_COGS = [IS_forecast[4]['Percent_COGS'], IS_forecast[1]['Percent_COGS'], IS_forecast[2]['Percent_COGS'],IS_forecast[3]['Percent_COGS']]
    Percent_Op_Exp = [IS_forecast[4]['Percent Op Exp'], IS_forecast[1]['Percent Op Exp'], IS_forecast[2]['Percent Op Exp'],IS_forecast[3]['Percent Op Exp']]
    Percent_SGA = [IS_forecast[4]['Percent SGA'], IS_forecast[1]['Percent SGA'], IS_forecast[2]['Percent SGA'],IS_forecast[3]['Percent SGA']]
    Percent_RandD = [IS_forecast[4]['Percent RandD'], IS_forecast[1]['Percent RandD'], IS_forecast[2]['Percent RandD'], IS_forecast[3]['Percent RandD']]
    Percent_Net_Income = [IS_forecast[4]['Percent Net Income'], IS_forecast[1]['Percent Net Income'], IS_forecast[2]['Percent Net Income'], IS_forecast[3]['Percent Net Income']]
elif Quarter_last == 'Q4':
    Percent_change = [IS_forecast[1]['Revenue Change'], IS_forecast[2]['Revenue Change'], IS_forecast[3]['Revenue Change'], IS_forecast[4]['Revenue Change']]
    Percent_COGS = [IS_forecast[1]['Percent_COGS'], IS_forecast[2]['Percent_COGS'], IS_forecast[3]['Percent_COGS'],IS_forecast[4]['Percent_COGS']]
    Percent_Op_Exp = [IS_forecast[1]['Percent Op Exp'], IS_forecast[2]['Percent Op Exp'], IS_forecast[3]['Percent Op Exp'],IS_forecast[4]['Percent Op Exp']]
    Percent_SGA = [IS_forecast[1]['Percent SGA'], IS_forecast[2]['Percent SGA'], IS_forecast[3]['Percent SGA'],IS_forecast[4]['Percent SGA']]
    Percent_RandD = [IS_forecast[1]['Percent RandD'], IS_forecast[2]['Percent RandD'], IS_forecast[3]['Percent RandD'], IS_forecast[4]['Percent RandD']]
    Percent_Net_Income = [IS_forecast[1]['Percent Net Income'], IS_forecast[2]['Percent Net Income'], IS_forecast[3]['Percent Net Income'], IS_forecast[4]['Percent Net Income']]
i = 0
while i < 4:
    Revenue_last += Revenue_last*Percent_change[i]
    COGS = Revenue_last*Percent_COGS[i]
    Op_Exp = Revenue_last*Percent_Op_Exp[i]
    SGA = Revenue_last*Percent_SGA[i]
    RandD = Revenue_last*Percent_RandD[i]
    Gross_Revenue = Revenue_last - COGS
    Op_Income = Gross_Revenue - Op_Exp
    Net_Income = Percent_Net_Income[i] * Op_Income
    Forecasted_revenue.append(Revenue_last)
    Forecasted_COGS.append(COGS)
    Forecasted_Op_Exp.append(Op_Exp)
    Forecasted_SGA.append(SGA)
    Forecasted_RandD.append(RandD)
    Forecasted_Gross_Revenue.append(Gross_Revenue)
    Forecasted_Op_Income.append(Op_Income)
    Forecasted_Net_Income.append(Net_Income)
    i+=1
if Quarter_last == 'Q1':
    Forecasted_revenue = {'Q2':Forecasted_revenue[0],
                          'Q3':Forecasted_revenue[1],
                          'Q4':Forecasted_revenue[2],
                          'Q1':Forecasted_revenue[3]}
    Forecasted_COGS = {'Q2':Forecasted_COGS[0],
                       'Q3':Forecasted_COGS[1],
                       'Q4':Forecasted_COGS[2],
                       'Q1':Forecasted_COGS[3]}
    Forecasted_Op_Exp = {'Q2':Forecasted_Op_Exp[0],
                         'Q3':Forecasted_Op_Exp[1],
                         'Q4':Forecasted_Op_Exp[2],
                         'Q1':Forecasted_Op_Exp[3]}
    Forecasted_SGA = {'Q2':Forecasted_SGA[0],
                      'Q3':Forecasted_SGA[1],
                      'Q4':Forecasted_SGA[2],
                      'Q1':Forecasted_SGA[3]}
    Forecasted_RandD = {'Q2':Forecasted_revenue[0],
                        'Q3':Forecasted_revenue[1],
                        'Q4':Forecasted_revenue[2],
                        'Q1':Forecasted_revenue[3]}
    Forecasted_Gross_Revenue = {'Q2':Forecasted_Gross_Revenue[0],
                        'Q3':Forecasted_Gross_Revenue[1],
                        'Q4':Forecasted_Gross_Revenue[2],
                        'Q1':Forecasted_Gross_Revenue[3]}
    Forecasted_Op_Income = {'Q2':Forecasted_Op_Income[0],
                        'Q3':Forecasted_Op_Income[1],
                        'Q4':Forecasted_Op_Income[2],
                        'Q1':Forecasted_Op_Income[3]}
    Forecasted_Net_Income = {'Q2':Forecasted_Net_Income[0],
                        'Q3':Forecasted_Net_Income[1],
                        'Q4':Forecasted_Net_Income[2],
                        'Q1':Forecasted_Net_Income[3]}
elif Quarter_last == 'Q2':
    Forecasted_revenue = {'Q3':Forecasted_revenue[0],
                          'Q4':Forecasted_revenue[1],
                          'Q1':Forecasted_revenue[2],
                          'Q2':Forecasted_revenue[3]}
    Forecasted_COGS = {'Q3':Forecasted_COGS[0],
                       'Q4':Forecasted_COGS[1],
                       'Q1':Forecasted_COGS[2],
                       'Q2':Forecasted_COGS[3]}
    Forecasted_Op_Exp = {'Q3':Forecasted_Op_Exp[0],
                         'Q4':Forecasted_Op_Exp[1],
                         'Q1':Forecasted_Op_Exp[2],
                         'Q2':Forecasted_Op_Exp[3]}
    Forecasted_SGA = {'Q3':Forecasted_SGA[0],
                      'Q4':Forecasted_SGA[1],
                      'Q1':Forecasted_SGA[2],
                      'Q2':Forecasted_SGA[3]}
    Forecasted_RandD = {'Q3':Forecasted_RandD[0],
                        'Q4':Forecasted_RandD[1],
                        'Q1':Forecasted_RandD[2],
                        'Q2':Forecasted_RandD[3]}
    Forecasted_Gross_Revenue = {'Q3':Forecasted_Gross_Revenue[0],
                        'Q4':Forecasted_Gross_Revenue[1],
                        'Q1':Forecasted_Gross_Revenue[2],
                        'Q2':Forecasted_Gross_Revenue[3]}
    Forecasted_Op_Income = {'Q3':Forecasted_Op_Income[0],
                        'Q4':Forecasted_Op_Income[1],
                        'Q1':Forecasted_Op_Income[2],
                        'Q2':Forecasted_Op_Income[3]}
    Forecasted_Net_Income = {'Q3':Forecasted_Net_Income[0],
                        'Q4':Forecasted_Net_Income[1],
                        'Q1':Forecasted_Net_Income[2],
                        'Q2':Forecasted_Net_Income[3]}
elif Quarter_last == 'Q3':
    Forecasted_revenue = {'Q4':Forecasted_revenue[0],
                          'Q1':Forecasted_revenue[1],
                          'Q2':Forecasted_revenue[2],
                          'Q3':Forecasted_revenue[3]}
    Forecasted_COGS = {'Q4':Forecasted_COGS[0],
                       'Q1':Forecasted_COGS[1],
                       'Q2':Forecasted_COGS[2],
                       'Q3':Forecasted_COGS[3]}
    Forecasted_Op_Exp = {'Q4':Forecasted_Op_Exp[0],
                         'Q1':Forecasted_Op_Exp[1],
                         'Q2':Forecasted_Op_Exp[2],
                         'Q3':Forecasted_Op_Exp[3]}
    Forecasted_SGA = {'Q4':Forecasted_SGA[0],
                      'Q1':Forecasted_SGA[1],
                      'Q2':Forecasted_SGA[2],
                      'Q3':Forecasted_SGA[3]}
    Forecasted_RandD = {'Q4':Forecasted_revenue[0],
                        'Q1':Forecasted_revenue[1],
                        'Q2':Forecasted_revenue[2],
                        'Q3':Forecasted_revenue[3]}
    Forecasted_Gross_Revenue = {'Q4':Forecasted_Gross_Revenue[0],
                        'Q1':Forecasted_Gross_Revenue[1],
                        'Q2':Forecasted_Gross_Revenue[2],
                        'Q3':Forecasted_Gross_Revenue[3]}
    Forecasted_Op_Income = {'Q4':Forecasted_Op_Income[0],
                        'Q1':Forecasted_Op_Income[1],
                        'Q2':Forecasted_Op_Income[2],
                        'Q3':Forecasted_Op_Income[3]}
    Forecasted_Net_Income = {'Q4':Forecasted_Net_Income[0],
                             'Q1':Forecasted_Net_Income[1],
                             'Q2':Forecasted_Net_Income[2],
                             'Q3':Forecasted_Net_Income[3]}
    
elif Quarter_last == 'Q4':
    Forecasted_revenue = {'Q1':Forecasted_revenue[0],
                          'Q2':Forecasted_revenue[1],
                          'Q3':Forecasted_revenue[2],
                          'Q4':Forecasted_revenue[3]}
    Forecasted_COGS = {'Q1':Forecasted_COGS[0],
                       'Q2':Forecasted_COGS[1],
                       'Q3':Forecasted_COGS[2],
                       'Q4':Forecasted_COGS[3]}
    Forecasted_Op_Exp = {'Q1':Forecasted_Op_Exp[0],
                         'Q2':Forecasted_Op_Exp[1],
                         'Q3':Forecasted_Op_Exp[2],
                         'Q4':Forecasted_Op_Exp[3]}
    Forecasted_SGA = {'Q1':Forecasted_SGA[0],
                      'Q2':Forecasted_SGA[1],
                      'Q3':Forecasted_SGA[2],
                      'Q4':Forecasted_SGA[3]}
    Forecasted_RandD = {'Q1':Forecasted_revenue[0],
                        'Q2':Forecasted_revenue[1],
                        'Q3':Forecasted_revenue[2],
                        'Q4':Forecasted_revenue[3]}
    Forecasted_Gross_Revenue = {'Q1':Forecasted_Gross_Revenue[0],
                        'Q2':Forecasted_Gross_Revenue[1],
                        'Q3':Forecasted_Gross_Revenue[2],
                        'Q4':Forecasted_Gross_Revenue[3]}
    Forecasted_Op_Income = {'Q1':Forecasted_Op_Income[0],
                        'Q2':Forecasted_Op_Income[1],
                        'Q3':Forecasted_Op_Income[2],
                        'Q4':Forecasted_Op_Income[3]}
    Forecasted_Net_Income = {'Q1':Forecasted_Net_Income[0],
                        'Q2':Forecasted_Net_Income[1],
                        'Q3':Forecasted_Net_Income[2],
                        'Q4':Forecasted_Net_Income[3]}
IS_Forecasted_Values = {'Revenue':Forecasted_revenue,
                       'COGS':Forecasted_COGS,
                       'Gross Revenue':Forecasted_Gross_Revenue,
                       'Op Exp':Forecasted_Op_Exp,
                       'SGA':Forecasted_SGA,
                       'RandD':Forecasted_RandD,
                       'Op Income':Forecasted_Op_Income,
                       'Net Income':Forecasted_Net_Income}
return IS_Forecasted_Values

def Projected_Income_Statement(Estimated_Forecast_Values):
Projected_Income_Statement = pd.DataFrame(Estimated_Forecast_Values)
return Projected_Income_Statement

IS_forecast = IS_Forecast(IS)
Estimated_Forecast_Values = Estimated_Forecast(IS_forecast,IS)
Projected_Income_Statement = Projected_Income_Statement(Estimated_Forecast_Values)

Projected_Income_Statement



sdfasdf