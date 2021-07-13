import xlrd


class ExcelUtil():
    def __init__(self,excelPath,sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        #获取第一行为key值
        self.keys = self.table.row_values(0)
        #获取总行数
        self.rowNum = self.table.nrows
        #获取总列数
        self.colNum = self.table.ncols

    def dict_date(self):
        if self.rowNum <=1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                #从第二行取对应的values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
            return r

    def get_rowinfo(self,row):
        '''获取exl中行信息,row--行数（int）'''
        if row <= 1:
            rowdata = None
        else:
            testdates = self.dict_date()
            rowdata = testdates[row-2]
        return rowdata

    def get_cellinfo(self,row,name):
        '''获取exl中某一单元格信息，row--行数（int）；name--列名(char)'''
        if row <= 1:
            rowdata = None
        else:
            testdates = self.dict_date()
            rowdata = testdates[row-2][name]
        return rowdata

    def get_xls_data(self, titlerow):
        '''自己写的获取xls表格中的数据,filepath--xls表格文件地址，titlerow--表头行数，如果内容是从第2行开始，那么就有1行表头，'''
        list = []
        for i in range(self.rowNum):
            xlsdata = self.get_rowinfo(i+titlerow)
            # print("xlsdata---------%s" %xlsdata)
            list.append(xlsdata)
            # print("--listdata--%s"%list)
        list = list[1:]

        print("----------list-----%s" %list)
        return list



if __name__ == "__main__":
    # filepath = "E:\\PyProject\\ZFAPI\\zongheshenji\\common\\datas.xls"
    # data = ExcelUtil(filepath)
    # testdates = data.dict_date()
    # # expect = testdates[1]["except"]
    # print(testdates[1]["department"])
    # # print(type(expect))
    filepath = "C:\\Users\\saloa\\Desktop\\TestDemo\\data\\qqEmail.xls"
    data = ExcelUtil(filepath)
    # list = []
    # for i in range(data.rowNum):# 一共有三行
    #     d = data.get_rowinfo(i+1)
    #     list.append(d)
    # print(list[1:])
    print("-----data%s" % data)
    d = data.get_xls_data(1)
    print("-------------%s" % d)