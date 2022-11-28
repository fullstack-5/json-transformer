#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json
import numpy as np
mapp = {}

	

def maketarget(ele,key,text):
	s= text
	if(isinstance(ele,list)==False):
		s+=f'["{key}"]'
	else:
		s+=f'[{key}]'
	
   
	if(isinstance(ele[key],dict)==False and isinstance(ele[key],list)==False):
				ele[key]=s
				return
	if(isinstance(ele[key],dict)):
		for k in ele[key]:
			maketarget(ele[key],k,s)		
	elif(isinstance(ele[key],list)):
		for i in range(len(ele[key])):
			maketarget(ele[key],i,s)





true = True
false = False


def checking(columnValue , i ,db) :
	if len(str(columnValue).split('ENUM')) >1 :
		columnValue1= columnValue.replace('ENUM(' , '')
		lis=columnValue1.split(')')
		listN=lis[0]
		if(len(lis)>1 and lis[1] !=''):
			return [handleEnum(listN , i ,db) ,lis[1]] 
		else :
			return handleEnum(listN , i , db)
	
	# if len(columnValue.split('IF')) >1 :
	#	 cmd_in_if = columnValue.split("IF(")[1].split(")")[0]
	#	 cmd_in_then = columnValue.split("THEN ")[1].split("ELSE")[0]
	#	 cmd_in_else = columnValue.split("ELSE ")[1] if len(columnValue.split("ELSE ")) > 1 else ""
	
	#	 ListFinal = [dotAndPlusSplit(cmd_in_if),dotAndPlusSplit(cmd_in_then),dotAndPlusSplit(cmd_in_else)]
	#	 print("list" , ListFinal)
		
	#	 return handle_if(ListFinal)
	
	return ''
		


def handleEnum(key,row_n , db):
	text =handleNormal(key)
	dicti =json.loads(db[db.columns[3]][row_n])
	return f"json.loads(db[db.columns[3]][{row_n}])[{text}]"

def handleNormal(str):
	last = False
	check=""
	list = dotAndPlusSplit(str)
  
	for i in list:
		if i not in ['+', "==", "-", "*", "/", "//"]:
			if(last):
				check+=f"['{i}']"
			else:
				check+=f"src['{i}']"
				last=True
			
		elif i=='+' :
			check+='+'
			last = False
		elif i in [ "==", "-", "*", "/", "//"]:
			check+=f"'{i}'"
			last=False
		 
	return check

def dotAndPlusSplit(str):
	st =str.replace('"','')
	dotSeparated=[]
	
	if("==" not in st and "." not in st and "+" not in st ):
		n_str=st.replace(' ','')
		dotSeparated.append(n_str)
		return dotSeparated
	if("=="in st):
		es=str.split('==')
		for p in range(len(es)):
			ps= es[p].split('+')
			for l in range(len(ps)):
				k=ps[l].replace(' ','').split('.')
				for i in range(1,len(k)):
					   dotSeparated.append(k[i])
				if(l!=len(ps)-1):
				   dotSeparated.append('+')
			if(p!=len(es)-1):
			   dotSeparated.append('==')
	else:
		ps= st.split('+')
		for l in range(len(ps)):
				k=ps[l].replace(' ','').split('.')
				for i in range(0,len(k)):
					   dotSeparated.append(k[i])
				if(l!=len(ps)-1):
				   dotSeparated.append('+')
				
	for l in dotSeparated:
		if l=='':
			dotSeparated.remove(l)
			
		
	
	return dotSeparated

# def handle_if_helper(list_of_instructions): #To Be Upgraded ........
#	 # List of instructions consider 
#	 # For solving IF
#	 print(src)
#	 checker = src.copy()
#	 py_code_if = ""
#	 structure = "src"
#	 request_for_else = False
#	 for i in list_of_instructions[0]:
#		 if i != "+" and i != "==":
#			 try:
#				 checker = checker[i]
#				 structure += f"[{i}]"
#			 except:
#				 request_for_else = True

#		 elif i in ["+", "==", "-", "*", "/", "//"]: 
#			 py_code_if += structure
#			 structure = "src"
#			 py_code_if += " " + str(i) + " "
#			 checker = src.copy()

#	 py_code_if += structure # Code structure for if statement.

#	 # =============================================
	
#	 checker = src.copy()
#	 structure = "src"
#	 py_code_then = ""
#	 for i in list_of_instructions[1]:
#		 # tester
#		 if i not in ["+", "==", "-", "*", "/", "//"]:
#			 checker = checker[i]
#			 structure += f"[{i}]"

#		 else: 
#			 py_code_then += structure
#			 structure = "src"
#			 py_code_then += " " + str(i) + " "
#			 checker = src.copy()
			
#	 py_code_then += structure # code structure for then statement

#	 # ==============================================

#	 checker = src.copy()
#	 structure = "src"
#	 py_code_else = ""
#	 if list_of_instructions[2] != "": 
#	 # only the code for then will come
#		 py_code_else = ""
#		 for i in list_of_instructions[1]:
#			 if i not in ["+", "==", "-", "*", "/", "//"]:
#				 checker = checker[i]
#				 structure += f"[{i}]"

#			 else: 
#				 py_code_else += structure
#				 structure = "src"
#				 py_code_else += " " + str(i) + " "
#				 checker = src.copy()
				
#		 py_code_else += structure # code structure for else statement

#	 if request_for_else == False:
#		 if list_of_instructions[2] == "":
#			 final_py_code = f"""
# if ({py_code_if}):
#	 {py_code_then}
# """
#		 else:
#			 final_py_code = f"""
# if ({py_code_if}):
#	 {py_code_then}
# else:
#	 {py_code_else}
# """

#	 else:
#		 final_py_code = f"""
# {py_code_else}
# """

#	 return final_py_code


# def handle_if(listOfInstruction) : 
#	 if 'items' in listOfInstruction[0] :
		
	
#	 else :
#		 return handle_if_helper(listOfInstruction)



def convert_to_code(src):
	with open('testing.py','w') as f_out:
		f_out.write('import json\n')
		f_out.write('target_json=')
		text=f'{src}'
		stack=[]
		rem_com=False
		tr_com=False
		for c in text:
			if c in ('{','(','[',':'):
				stack.append(c)
			if stack[-1]=='{':
					rem_com=False
			else:
				rem_com=True
			if stack[-1]==':':
				rem_com=True
			
			if(c==':'):
				rem_com=True
			if((c==','or c=='}')and stack[-1]==':'):
				stack.pop(-1)
			if(c!='"'):
				f_out.write(c)
			else:
				if rem_com==False:
					f_out.write(c)
				
			if c in ('}',')',']') :
				stack.pop(-1)
			

		f_out.write('\n')
		f_out.write('n_target_json=json.dumps(target_json)\n')
		f_out.write("with open('generated.json', 'w') as json:\n")
		f_out.write("\tjson.write(n_target_json)")


def code_generator(source, target, mapping):
	with open(mapping.name, 'r') as f_in, open('sample.tsv', 'w') as f_out:

		content = f_in.read().replace('","',"@!").replace(',','\t').replace("@!", ',')
		f_out.write(content)

	db = pd.read_table("sample.tsv")

	with open(source.name , 'r') as source :
		src=json.load(source)

	with open(target.name , 'r') as target :
		trg = json.load(target)
	trg_final = trg.copy()
	for k in trg_final:
		   maketarget(trg_final,k,"src")
	
	for i in range(len(db)) : 
		columnValues = db[db.columns[2]][i]
		jsonValues = checking(columnValues , i , db)
		if type(jsonValues) != type("str") : 
			finalJason = jsonValues[0] + handleNormal(jsonValues[1])
		else :
			if jsonValues == '' and len(str(columnValues).split('IF')) > 1 :
				finalJason = None
			elif jsonValues == '' :
				finalJason = handleNormal(str(columnValues))
			else :
				finalJason = jsonValues 
				
			
   
	
		newJasonKeys = str(db[db.columns[1]][i])
		listEntry = dotAndPlusSplit(newJasonKeys)


		if len(listEntry) == 1 :
			trg_final[listEntry[0]] = finalJason

		else : 
			if isinstance(trg_final[listEntry[0]] , list) :
				for i in range(len(trg_final[listEntry[0]])) :
					iter =trg_final[listEntry[0]][i] 
					for j in range(len(listEntry)-1):
						if j == len(listEntry) - 2  :
							iter[listEntry[j+1]] = finalJason
						else :
							iter = iter[listEntry[j+1]]

			else :
				iter = trg_final[listEntry[0]]
				for i in range(len(listEntry)-1):
					if i == len(listEntry) - 2  :
						iter[listEntry[i+1]] = finalJason
					else :
						iter = iter[listEntry[i+1]]		  

	convert_to_code(trg_final)
	with open('testing.py' , 'r') as fr :
		file = fr.read()
		
	
	name = source.name + "@" + "we_are_fullstack5"
	mapp[name] = trg_final
	return (file, name)


def code_executor(source , specification):
	with open(source.name , 'r') as source :
		src=json.load(source)
		
	db = pd.read_table("sample.tsv")
	with open('testing2.py','w') as f_out:	
		f_out.write("import json\n")
		f_out.write("def fin(src, db):\n")
		f_out.write("\tfinal=")
		obj = mapp[str(specification)]
		text=f'{obj}'
		stack=[]
		rem_com=False
		tr_com=False
		for c in text:
			if c in ('{','(','[',':'):
				stack.append(c)
			if stack[-1]=='{':
					rem_com=False
			else:
				rem_com=True
			if stack[-1]==':':
				rem_com=True
			if(c==':'):
				rem_com=True
			if((c==','or c=='}')and stack[-1]==':'):
				stack.pop(-1)
			if(c!='"'):
				f_out.write(c)
			else:
				if rem_com==False:
					f_out.write(c)
			if c in ('}',')',']') :
				stack.pop(-1)
		f_out.write("\n\treturn final")
# 	with open('testing2.py' , 'r') as fr :
# 		file = fr.read()
	import testing2
	return testing2.fin(src,db)

	
	
	


# In[2]:


import pandas as pd
import gradio as gr



def main():
    inter1 = gr.Interface(fn = code_generator,
                        inputs=[gr.inputs.File(label="Source JSON File"), gr.inputs.File(label="Target JSON File"), gr.inputs.File(label="Mapping CSV File")],
                        outputs=[gr.outputs.Textbox(label = "Generated Code"), gr.outputs.Textbox(label = "generated Code Specification")],
    theme = "huggingface",
    title = "Fullstack5",
    description = "Enter 3 files as input:\n1. Source JSON\n2. Target JSON\n3. Mapping CSV File",
    allow_flagging = False)
    
    inter2 = gr.Interface(fn = code_executor,
                        inputs=[gr.inputs.File(label="Source JSON File"), gr.inputs.Textbox(label = "Specification Name")],
                        outputs=[gr.outputs.Textbox(label="Target JSON retrieved")],
    theme = "huggingface",
    title = "Fullstack5",
    description = "Enter Source JSON file and Mapping Specification",
    allow_flagging = False)
    
    tabbed_interface = gr.TabbedInterface(interface_list = [inter1, inter2],
                                         tab_names = ["Code generator", "Code Executor"])
    
    tabbed_interface.launch()

main()


# In[ ]:




