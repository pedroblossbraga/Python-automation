"""
==================================
Statistical report over a csv file
==================================
"""


import pandas as pd
import numpy as np
from scipy import stats
from pandas import DataFrame
from datetime import datetime
import os

end = str(input('Add the complete path and file name to be analyzed: '+'\n'))

def relatorio_txt(end):	

	def porcent_unique(col_name):
		return str('% de unique: '+ str(100*len(df[col_name].unique())/len(df[col_name]))+' %')

	def gera_data_atual():
			# datetime object containing current date and time
			now = datetime.now()
			 
			#print("now =", now)
			# dd/mm/YY H:M:S
			data = now.strftime("%d%m%Y")
			hora = now.strftime("%H%M%S")
			d1 = str(data+'_'+hora)
			#dt_string = now.strftime("%d%m%Y_%H%M%S")
			print("d1 =", d1)
			return d1

	df = pd.read_csv(end, sep=',', encoding='utf-8')

	#df = df.dropna(how=any)
	def acha_datas(df):
		datas=[]
		for k in range(len(df.columns)):
			#for j in range(len(df[df.columns[k]])):
			for i in range(len(str(df[df.columns[k]][1]))):
				if len(str(df[df.columns[k]][1])) == 10:
					# Para caso as datas sejam do tipo aaaa/mm/dd ou dd/mm/aaaa ou aaaa-mm-dd ou dd-mm-aaaa

					if str(df[df.columns[k]][1])[4] == str("-") and str(df[df.columns[k]][1])[7] == str("-"):
						#print('O elemento ', str(df[df.columns[k]][j]) ,' possui -')
						datas = df.columns[k]
						return datas	

					if str(df[df.columns[k]][1])[2] == str("-") and str(df[df.columns[k]][1])[5] == str("-"):
						#print('O elemento ', str(df[df.columns[k]][j]) ,' possui -')
						datas = df.columns[k]
						return datas	

					if str(df[df.columns[k]][1])[4] == str("/") and str(df[df.columns[k]][1])[7] == str("/"):
						#print('O elemento ', str(df[df.columns[k]][j]) ,' possui -')
						datas = df.columns[k]
						return datas	

					if str(df[df.columns[k]][1])[2] == str("/") and str(df[df.columns[k]][1])[5] == str("/"):
						#print('O elemento ', str(df[df.columns[k]][j]) ,' possui -')
						datas = df.columns[k]
						return datas

				if len(str(df[df.columns[k]][1])) == 6:
					if str(df[df.columns[k]][1])[4] == str("-"):
						# aaaa-mm
						datas = df.columns[k]
						return datas	

					if str(df[df.columns[k]][1])[4] == str("/"):
						# aaaa/mm
						datas = df.columns[k]
						return datas	

					if str(df[df.columns[k]][1])[2] == str("-"):
						# mm-aaaa
						datas = df.columns[k]
						return datas	

					if str(df[df.columns[k]][1])[4] == str("/"):
						# mm/aaaa
						datas = df.columns[k]
						return datas
			# Procurando datas do tipo int
			try:
				# Agora caso as datas sejam aaaammdd ou ddmmaaaa
				if len(str(df[df.columns[k]][1])) == 8: #and int(df[df.columns[k]][1]) % 1 >0:
					#ddmmaaaa
					if (int(str(df[df.columns[k]][1])[0:2]) <= 31 or int(str(df[df.columns[k]][1])[0:2]) >= 2000 or int(str(df[df.columns[k]][1])[0:2]) <= 12) and int(str(df[df.columns[k]][1])[0:2]) > 0:
						if (int(str(df[df.columns[k]][1])[2:4]) <= 31 or int(str(df[df.columns[k]][1])[2:4]) >= 2000 or int(str(df[df.columns[k]][1])[2:4]) <= 12) and int(str(df[df.columns[k]][1])[2:4]) > 0:
							if (int(str(df[df.columns[k]][1])[4:8]) <= 31 or int(str(df[df.columns[k]][1])[4:8]) >= 2000 or int(str(df[df.columns[k]][1])[4:8]) <= 12) and int(str(df[df.columns[k]][1])[4:8]) > 0:
								datas = df.columns[k]
								return datas	
									
					#aaaammdd
					if (int(str(df[df.columns[k]][1])[0:4]) <= 31 or int(str(df[df.columns[k]][1])[0:4]) >= 2000 or int(str(df[df.columns[k]][1])[0:4]) <= 12) and int(str(df[df.columns[k]][1])[0:4]) > 0:
						if (int(str(df[df.columns[k]][1])[4:6]) <= 31 or int(str(df[df.columns[k]][1])[4:6]) >= 2000 or int(str(df[df.columns[k]][1])[4:6]) <= 12) and int(str(df[df.columns[k]][1])[4:6]) > 0:
							if (int(str(df[df.columns[k]][1])[6:8]) <= 31 or int(str(df[df.columns[k]][1])[6:8]) >= 2000 or int(str(df[df.columns[k]][1])[6:8]) <= 12) and int(str(df[df.columns[k]][1])[6:8]) > 0:
								datas = df.columns[k]
								return datas	
									
				# Caso a data seja do tipo aaaamm
				if len(str(df[df.columns[k]][1])) == 6: #and int(df[df.columns[k]][1]) % 1 >0:
					if int(str(df[df.columns[k]][1])[0:4])  >= 2000:
						if int(str(df[df.columns[k]][1])[4:6]) <= 12:
							if int(str(df[df.columns[k]][1])[4:6]) > 0:
								datas = df.columns[k]
								return datas	
					#ddmmaaaa
					#print('PASSOU INT')
					if  int(str(df[df.columns[k]][1])[0:2]) <= 12:
						if int(str(df[df.columns[k]][1])[0:2]) > 0:
							if int(str(df[df.columns[k]][1])[2:6]) >= 2000:
								datas = df.columns[k]
								return datas
								
				print(' ', '\n', 'The date column is ', '\n', ' ', datas, '\n', ' ', '\n')	
			except: print('There is no date column in the format aaaammmddd ou ddmmaaaa. ')

		return datas
	datas = acha_datas(df)
	if len(datas) >0:
		df_data = df.groupby([datas]).sum()
	#df_data = df_data.drop(['Unnamed: 0'], axis = 1)

	def main():
		data_str = gera_data_atual()
		enddir = str(input('Insert the report directory: '+'\n'))

		nome = enddir+'Report'+data_str+".txt"
		f = open(nome, "a+")

		f.write((str("Report"+"\n"+ " "+ "\n"+ " " + "\n").center(80)))

		f.write("Infos:"+"\n"+2*len("Informações gerais do Arquivo de entrada:")*"_"+"\n"+" "+"\n")
		f.write("The file contains"+ str(df.shape[0])+" lines, and "+ str(df.shape[1])+" columns."+ " \n"+ " " + "\n")

		f.write(("The columns are: " + "\n" + " " + "\n").center(80))
		f.write((str(df.columns)+ "\n" + " " + "\n").center(80))

		f.write(str(df.info())+'\n'+' '+'\n')

		f.write(" "+"\n"+ 180*"-" + "\n" + " "+ "\n")

		f.write('# NaNs (count): '+str(df.isna().sum())+ '\n'+' '+'\n')

		f.write(('Value informations: '+'\n'+2*len('Value informations: ')*'_'+'\n'+' '+'\n').center(80))
		for k in range(len(df.columns)):
			f.write(('COLUMN: ' + df.columns[k].upper() + '\n'+' '+ '\n').center(80))

			if type(df[df.columns[k]][0]) != str or type(df[df.columns[k]][1]) != str:
				f.write(('Mean: '+str(df[df.columns[k]].dropna(how='any').mean()) +'\n'+' '+'\n').center(80))
				f.write(('Max: '+str(df[df.columns[k]].dropna(how='any').max()) +'\n'+' '+'\n').center(80))
				f.write(('Min: '+str(df[df.columns[k]].dropna(how='any').min()) +'\n'+' '+'\n').center(80))
				f.write(('Std: '+str(df[df.columns[k]].std()) +'\n'+' '+'\n').center(80))

			f.write('total: '+str(len(df[df.columns[k]]))+' , with '+str(len(df[df.columns[k]].unique()))+' unique values. '+'\n'+' '+'\n')

			f.write(('Qtd Unique values: '+str(len(df[df.columns[k]].unique())) +'\n'+' '+'\n').center(80))
			f.write(('% Unique: '+str(porcent_unique(df.columns[k])) +'\n'+' '+'\n').center(80))
			f.write(('Most frequent (Mode): '+str(df[df.columns[k]].mode().values)).center(80))

			f.write(' ' + '\n' + 180*'_' + '\n'+ ' ' + '\n'+ ' ')

		if len(datas)>0:
			f.write(('Date infos: '+'\n'+2*len('Date infos: ')*'_'+'\n'+' '+'\n').center(80))
			
			for k in range(len(df_data.columns)):
				f.write((str(df_data.columns[k])+'\n').center(80))
				f.write((str(df_data[df_data.columns[k]].describe())+'\n').center(80))
				f.write(' '+'\n')
		else:
			f.write(' ' + '\n')
			f.write('Aparently, we did not found the date column.'.center(100))
			f.write( '\n'+ ' ')

		f.close()
	if __name__ =="__main__":
		print(__doc__)
		main()

relatorio_txt(end) 
