from docx import Document
from docx.shared import Inches,Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
#调用自带的库
def genPaper(_Name='试卷.docx'):      #试卷生成
    Doc=Document()

    #标题 
    Title=Doc.add_paragraph('南 京 航 空 航 天 大 学')   
    Title.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    Title.style.font.name=u'楷体'
    Title.style.element.rPr.rFonts.set(qn('w:eastAsia'), '楷体')
    Title.style.font.size=Pt(22)
    Title.style.font.bold=True

    #页码
    Page=Doc.add_paragraph('')




    Doc.save(_Name)
def genAnswer(_Name='答案.docx'):     #答案生成
    doc=Document()
    #todo
    doc.save(_Name)
genPaper()

'''                                                 #大杀器 调用默认word软件
import win32com
from win32com.client import Dispatch, constants
import os,sys
W = win32com.client.Dispatch('Word.Application')
W.Visible = 0
W.DisplayAlerts = 0
Doc = W.Documents.Open( '%s\\sjmb.docx' %sys.path[0])
Doc.Close()
W.Quit()
'''