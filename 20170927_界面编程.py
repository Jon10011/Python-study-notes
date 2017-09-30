#coding=utf-8
from Tkinter import *
root = Tk()
V = IntVar()
V.set(2)#设置位置
Radiobutton(root,text='range',variable=V,value=1).pack(anchor=W)#W放在中间
Radiobutton(root,text='if',variable=V,value=2).pack(anchor=W)
Radiobutton(root,text='while',variable=V,value=3).pack(anchor=W)
var = IntVar()
c =Checkbutton(root,text='this is int',variable=var)
c1 =Checkbutton(root,text='this is int',variable=var)
c.pack()
c1.pack()
e = Entry(root)
e.pack(padx = 20,pady = 20)
e.delete(0,END)#delete(first,last-None)删除参数first到last的所有内容,e.delete(0,END)表示删除输入框的所有内容
e.insert(0,'请在此输入......')#insert(index,text)将text参数插入到index参数的指定位置
listbox = Listbox(root)
listbox.pack(fill=BOTH,expand=True)#True指定填充父组件的剩余空间 BOTH填充方式
Label(root,text='Red',bg='red',fg='white').pack(fill=X)
Label(root,text='Green',bg='green',fg='black').pack(fill=X)
Label(root,text='Blue',bg='blue',fg='white').pack(side=RIGHT)
"""
pack():
anchor:控制组件在pack分配空间的位置(N,NE,S,SW)
fill:指定是否填充父组件额外的空间
side:指定组件放置的位置，默认是TOP(LEFT,BOTTOM,RIGHT)
"""
#Label(root,text='123').grid(row=0)
#Label(root,text='321').grid(row=2)
#Entry(root).grid(row=0,column=1)
#Entry(root).grid(row=1,column=1)
for i in range(10):
    listbox.insert(END,str(i))
#def callback():
    #print 'int is nobody'
#b = Button(root,text='谁',height = 1,width = 6,command = callback)
#b.pack(side = BOTTOM)
#label = Label(root,text = 'hello Tkinter')
#label.pack()
root.mainloop()
"""
创建并运行GUI模块的5步基本
    1导入Tkinter模块
    2创建一个顶层窗口对象，来容纳整个GUI程序
    3在顶层窗口对象上（或者其中）创建所有的GUI模块（及功能）
    4把这些GUI模块与底层程序代码相连接
    5进入主事件循环
"""
"1.label标签组件用于在屏幕上显示文字，label仅能显示单一字体，但文本可以换行"
"2.button组件用于实现各种各样的按钮"
"3.单选、复选框" \
"   Radiobutton单选按钮组件实现多选一的问题" \
"   Checkbutton组件用于实现确定是否选择的按钮"
"4.输入框,Entyr"
"5.pack，grid,place用于管理组件布局"
"   pack 按照添加顺序排列组件"
"   Grid 按照行/列形式怕列组件"
"   Place 允许程序员指定组件的大小和位置" \
"       何时使用pack管理器？组件比较少的情况下"

