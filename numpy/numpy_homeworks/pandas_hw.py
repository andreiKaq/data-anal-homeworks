import numpy as np
import pandas as pd
import matplotlib as plt
df = pd.read_csv('baltics_dividends.csv', delimiter=',')



#1. Установите столбец ticker в качестве нового индекса DataFrame.

df = df.set_index('ticker')


#2. Выведите матрицу корреляции. Какой признак больше всего коррелирует с dividend_max?

new_corr = df.select_dtypes('number').corr()
# print(new_corr['dividend_max'])


#3. Найдите среднее и медиану по столбцу dividend_count.

# print(df['dividend_count'].mean())
# print(df['dividend_count'].median())




#4. Какой процент компаний начал выплачивать дивиденды после 2018 года?

comps = len(df)
comps_after = df[df['years_from'] >= 2019].count()
percent = (comps_after / comps) * 100

# print('Тут процент компаний которые начали выплачивать дивиденды после 2018 года: ', percent)





#5. Какова самая высокая цена среди латвийских компаний?

latvia_prices = df[df['market'] == 'RIG']['price']
most_high_price = latvia_prices.values.max()
# print(most_high_price)

#6. Выведите DataFrame с ticker, первым и последним годами выплаты дивидендов для компаний со средней справедливой ценой от 4 до 11.               !!!!!!!!!

fair_price_comps = (df['fair_price_avg'] > 4) & (df['fair_price_avg'] <= 11)
sorted_df = df[fair_price_comps]
answer_df = sorted_df[['dividend_min', 'dividend_max']]

# print(answer_df)
# print(df.dtypes, df['dividend_min'])

#7. Замените значения market на Estonia, Latvia и Lithuania.
df['market'] = df['market'].replace({
    'RIG': 'Latvia',
    'TLN': 'Tallinn',
    'VLN': 'Lithuania'
})
# print(df['market'])
#8. Посчитайте количество лет с выплатами дивидендов (total_years) и отсортируйте их по возрастанию.
sorted_values = df.sort_values('total_years')

# print(sorted_values['total_years'])

#9. Создайте новый столбец 'dividend_avg', используя dividend_min и dividend_max, и вставьте его после столбца dividend_max.

df['dividend_avg'] = (df['dividend_min'] + df['dividend_max']) / 2
cols = list(df.columns)
insert_at = cols.index('dividend_max') + 1

cols.insert(insert_at, cols.pop(cols.index('dividend_avg')))
df = df[cols]
# print(df['dividend_avg'])
# print(df['dividend_min'])

#10. Сгруппируйте DataFrame по рынку и году начала выплат дивидендов, затем просуммируйте годовые выплаты по каждой группе.

grouped = df.groupby(['market', 'years_from'])['annual_payout'].sum()
# print(grouped)


#11. Сгруппируйте DataFrame по рынку и создайте новый DataFrame, отображающий минимум и максимум годовых выплат, а также среднюю и медианную цену для каждой группы.
grouped_df = df.groupby(['market']).agg({
    'annual_payout': ['min', 'max'],
    'price': ['mean', 'median'],
})

print(grouped_df)

