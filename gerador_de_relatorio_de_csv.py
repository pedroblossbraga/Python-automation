import pandas as pd
import numpy as np
from scipy import stats
from pandas import DataFrame
from datetime import datetime
import os

end = str(input('Insira o caminho completo com o nome do arquivo para analisar: '+'\n'))

def relatorio_txt(end):	

	def porcent_unique(col_name):
		return str('Porcentagem de unique: '+ str(100*len(df[col_name].unique())/len(df[col_name]))+' %')

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
								
				print(' ', '\n', 'A coluna de datas é a ', '\n', ' ', datas, '\n', ' ', '\n')	
			except: print('Não ha coluna com datas do tipo aaaammmddd ou ddmmaaaa. ')

		return datas
	datas = acha_datas(df)
	if len(datas) >0:
		df_data = df.groupby([datas]).sum()
	#df_data = df_data.drop(['Unnamed: 0'], axis = 1)

	def main():
		data_str = gera_data_atual()
		enddir = str(input('Insira o caminho do relatorio: '+'\n'))

		nome = enddir+'Relatorio'+data_str+".txt"
		f = open(nome, "a+")

		f.write((str("Relatório da base Oriana_ 13112019_1635_Hirota_amostra_bebidas_loja3.csv"+"\n"+ " "+ "\n"+ " " + "\n").center(80)))

		f.write("Informações gerais do Arquivo de entrada:"+"\n"+2*len("Informações gerais do Arquivo de entrada:")*"_"+"\n"+" "+"\n")
		f.write("O Arquivo de entrada contém "+ str(df.shape[0])+" linhas, e "+ str(df.shape[1])+" colunas."+ " \n"+ " " + "\n")

		f.write(("Suas colunas sao: " + "\n" + " " + "\n").center(80))
		f.write((str(df.columns)+ "\n" + " " + "\n").center(80))

		f.write(str(df.info())+'\n'+' '+'\n')

		f.write(" "+"\n"+ 180*"-" + "\n" + " "+ "\n")

		f.write('Contagem de NaNs: '+str(df.isna().sum())+ '\n'+' '+'\n')

		f.write(('Informações dos valores: '+'\n'+2*len('Informações dos valores: ')*'_'+'\n'+' '+'\n').center(80))
		for k in range(len(df.columns)):
			f.write(('COLUNA: ' + df.columns[k].upper() + '\n'+' '+ '\n').center(80))

			if type(df[df.columns[k]][0]) != str or type(df[df.columns[k]][1]) != str:
				f.write(('Media: '+str(df[df.columns[k]].dropna(how='any').mean()) +'\n'+' '+'\n').center(80))
				f.write(('Max: '+str(df[df.columns[k]].dropna(how='any').max()) +'\n'+' '+'\n').center(80))
				f.write(('Min: '+str(df[df.columns[k]].dropna(how='any').min()) +'\n'+' '+'\n').center(80))
				f.write(('Desvio Padrão: '+str(df[df.columns[k]].std()) +'\n'+' '+'\n').center(80))

			f.write('total: '+str(len(df[df.columns[k]]))+' , com '+str(len(df[df.columns[k]].unique()))+' valor(es) único(s). '+'\n'+' '+'\n')

			#f.write(('Unicos: :'+'\n')
			#for j in range(len(df[df.columns[k]].unique())):
				#f.write(str(df[df.columns[k]].unique()[j]) +'\n')
			#f.write(' '+'\n')
			#f.write(('Unicos: '+str(df[df.columns[k]].unique()) +'\n'+' '+'\n').center(80))
			f.write(('Qtd Unicos: '+str(len(df[df.columns[k]].unique())) +'\n'+' '+'\n').center(80))
			f.write(('Porcentagem de Unicos: '+str(porcent_unique(df.columns[k])) +'\n'+' '+'\n').center(80))
			f.write(('Mais frequente (Moda): '+str(df[df.columns[k]].mode().values)).center(80))

			f.write(' ' + '\n' + 180*'_' + '\n'+ ' ' + '\n'+ ' ')

		if len(datas)>0:
			f.write(('Informações relativas às datas: '+'\n'+2*len('Informações relativas às datas: ')*'_'+'\n'+' '+'\n').center(80))
			
			for k in range(len(df_data.columns)):
				f.write((str(df_data.columns[k])+'\n').center(80))
				f.write((str(df_data[df_data.columns[k]].describe())+'\n').center(80))
				f.write(' '+'\n')
		else:
			f.write(' ' + '\n')
			f.write('Aparentemente, não encontrou a coluna de datas.'.center(100))
			f.write( '\n'+ ' ')

		'''
		for j in range(len(df_data.columns)):
			f.write(str(df_data.columns[j]).center(80)+'\n'+' '+'\n')
			f.write(' '+'\n'+' '+'\n')
			for i in range(len(df_data)):
				data=[]
				data.append((str(df_data.index[i])+' : '+(str(df_data[df_data.columns[j]][i]))).center(80))
				f.write((str(data))+'\n'+' '+'\n')
			f.write(' ' + '\n' + 180*'_' + '\n'+ ' ' + '\n'+ ' ')
		'''

		f.close()
	if __name__ =="__main__":
		main()

relatorio_txt(end) 
