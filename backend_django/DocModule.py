from docx import Document
from docx.shared import Inches,Pt,Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT,WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
#添加分数框
def addPoint(Cell):
    Table=Cell.add_table(rows=2,cols=2)
    Table.style='Table Grid'
    
    Table.rows[0].height=Cm(0.82)
    Table.rows[1].height=Cm(0.82)
    Table.columns[0].width=Cm(2.12)
    Table.columns[1].width=Cm(1.56)
    Table.autofit=False

    Para=Table.cell(0,0).paragraphs[0]
    Para.add_run('本题分数')
    Para.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    Table.cell(0,0).vertical_alignment = WD_ALIGN_VERTICAL.CENTER

    Para=Table.cell(1,0).paragraphs[0]
    Para.add_run('得   分')
    Para.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    Table.cell(1,0).vertical_alignment = WD_ALIGN_VERTICAL.CENTER

#调用自带的库
def genPaper(_Name='试卷.docx'):      #试卷生成
    Doc=Document('模板.docx')
    '''
    #标题 
    Title=Doc.paragraphs[0]   
    Title.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    Title.paragraph_format.space_before=Pt(14)
    Run=Title.add_run('南 京 航 空 航 天 大 学')
    Run.font.name=u'楷体'
    Run.element.rPr.rFonts.set(qn('w:eastAsia'), '楷体')
    Run.font.size=Pt(22)
    Run.font.bold=True

    #页码
    Page=Doc.add_paragraph()
    Page.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    Run=Page.add_run('第1页 （共2页）')
    Run.font.size=Pt(10.5)
    Run.font.name=u'宋体'  
    Run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    Run.font.bold=False
    '''
  
    #整张卷子
    #卷头
    Table=Doc.tables[0]
    #Table.style=Doc.styles['Table Grid' ]

    Para=Table.cell(0,0).paragraphs[0]
    Para.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    Run=Para.add_run('二○○  ～ 二○○ 学年  第 学期')         #todo
    Run.font.size=Pt(10.5) 
    Run.font.name=u'宋体'
    Run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    Run.bold=False

    Run=Para.add_run('《     》考试试题')
    Run.font.size=Pt(18) 
    Run.font.name=u'楷体'
    Run.element.rPr.rFonts.set(qn('w:eastAsia'), '楷体')
    Run.bold=True

    Para=Table.cell(0,0).paragraphs[1]
    
    Run=Para.add_run('考试日期： 年 月 日     试卷类型：        试卷代号：')
    Run.font.size=Pt(10.5) 
    Run.font.name=u'宋体'
    Run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    Run.bold=False

    #分数框
    addPoint(Table.cell(4,0))
    #todo

    Doc.save(_Name)
def genAnswer(_Name='答案.docx'):     #答案生成
    Doc=Document('答案模板.docx')

    #卷头
    Table=Doc.tables[0]

    Para=Table.cell(0,0).paragraphs[0]
    Run=Para.add_run('二○○  ～ 二○○  学年   第   学期')
    Run.font.size=Pt(13)
    Run.font.name=u'宋体'
    Run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    Run.bold=False

    Para=Table.cell(0,0).paragraphs[1]
    Run=Para.add_run('课程名称：')
    Run.font.size=Pt(13)
    Run.font.name=u'宋体'
    Run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    Run.bold=False

    Run=Para.add_run('《               》参考答案及评分标准')
    Run.font.size=Pt(18)
    Run.font.name=u'楷体'
    Run.element.rPr.rFonts.set(qn('w:eastAsia'), '楷体')
    Run.bold=True

    Para=Table.cell(0,0).paragraphs[2]
    Run=Para.add_run('命题教师：                 试卷类型：        试卷代号：')
    Run.font.size=Pt(13)
    Run.font.name=u'宋体'
    Run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    Run.bold=False

    #todo
    Doc.save(_Name)
genAnswer()

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