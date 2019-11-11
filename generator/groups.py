from comtypes.client import CreateObject
import os

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

#creat10 rows and save in excel

xl = CreateObject("Excel.Application")
xl.Visible = 1
wb = xl.Workbooks.Add()
for i in range(10):
    #диапазон ячеек     xl.Range["A1", "C1"].Value[()] =
    xl.Range["A%s"%(i+1)].Value[()] = "group %s"%i
wb.SaveAs(os.path.join(project_dir,"groups.xlsx"))
xl.Quit()