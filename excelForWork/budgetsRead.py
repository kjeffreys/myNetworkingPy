import openpyxl

def getKakiat():
    wb = openpyxl.load_workbook('C:/Users/aj282/Downloads/School budget proposals/School budget proposals/Kakiat Budget 2020 ERCSD- principal budget.xlsx', data_only=True)

    sheet = wb['Sheet1']

    #sheetsDict = {}

    rowNum = 1

    wb2 = openpyxl.Workbook()
    sheet2 = wb2.active
    sheet2.title = 'Aggregate'
    row2 = 1
    #Technology Hardware
    for i in range(31,38):
        rowNum = i
        cell = 'E' + str(rowNum)
        if sheet[cell].value == None:
            #print("Empty cell: {}".format(cell))
            continue
        else:
            print()
            quant = 'G' + str(rowNum)
            cost = 'H' + str(rowNum)
            value = str(sheet[quant].value) + " ($" + str(sheet[cost].value) + ")"
            print("{}: {}".format(cell, sheet[cell].value))
            row2 += 1
            sheet2CellA = 'A' + str(row2)
            sheet2CellB = 'B' + str(row2)
              
            if sheet[cell].value.find(":") != -1:
                print("{}: {}".format(cell, sheet[cell].value[:sheet[cell].value.find(":")]))
                sheet2[sheet2CellA] = sheet[cell].value[:sheet[cell].value.find(":")]
                sheet2[sheet2CellB] = value
            else:
                print("{}: {}...{}".format(cell, sheet[cell].value[:30], value))
                sheet2[sheet2CellA] = sheet[cell].value[:30]
                sheet2[sheet2CellB] = value
            


    #Technology Software
    for i in range(70,81):
        print("\nBegin software\n")
        rowNum = i
        cell = 'E' + str(rowNum)
        if sheet[cell].value == None:
            #print("Empty cell: {}".format(cell))
            continue
        else:
            print()
            quant = 'G' + str(rowNum)
            cost = 'H' + str(rowNum)
            value = str(sheet[quant].value) + " ($" + str(sheet[cost].value) + ")"
            print("{}: {}".format(cell, sheet[cell].value))
            row2 += 1
            sheet2CellA = 'A' + str(row2)
            sheet2CellB = 'B' + str(row2)
              
            if sheet[cell].value.find(":") != -1:
                print("{}: {}".format(cell, sheet[cell].value[:sheet[cell].value.find(":")]))
                sheet2[sheet2CellA] = sheet[cell].value[:sheet[cell].value.find(":")]
                sheet2[sheet2CellB] = value
            else:
                print("{}: {}...{}".format(cell, sheet[cell].value[:30], value))
                sheet2[sheet2CellA] = sheet[cell].value[:30]
                sheet2[sheet2CellB] = value
    
    wb2.save('C:/Users/aj282/kakiat.xlsx')

def getSvhs():
    wb = openpyxl.load_workbook('C:/Users/aj282/Downloads/School budget proposals/School budget proposals/SVHS-ERCSD-budget-principal_form.xlsx', data_only=True)

    sheet = wb['Sheet1']

    #sheetsDict = {}

    rowNum = 1

    wb2 = openpyxl.Workbook()
    sheet2 = wb2.active
    sheet2.title = 'Aggregate'
    row2 = 1

    #Technology Hardware (Note: Other hardware/bad data to be filtered)
    for i in range(57,137):
        rowNum = i
        cell = 'E' + str(rowNum)
        if sheet[cell].value == None:
            #print("Empty cell: {}".format(cell))
            continue
        else:
            print()
            quant = 'G' + str(rowNum)
            cost = 'H' + str(rowNum)
            value = str(sheet[quant].value) + " ($" + str(sheet[cost].value) + ")"
            print("{}: {}".format(cell, sheet[cell].value))
            row2 += 1
            sheet2CellA = 'A' + str(row2)
            sheet2CellB = 'B' + str(row2)
              
            if sheet[cell].value.find(":") != -1:
                print("{}: {}".format(cell, sheet[cell].value[:sheet[cell].value.find(":")]))
                sheet2[sheet2CellA] = sheet[cell].value[:sheet[cell].value.find(":")]
                sheet2[sheet2CellB] = value
            else:
                print("{}: {}...{}".format(cell, sheet[cell].value[:30], value))
                sheet2[sheet2CellA] = sheet[cell].value[:30]
                sheet2[sheet2CellB] = value
            


    #Technology Software
    for i in range(140,144):
        print("\nBegin software\n")
        rowNum = i
        cell = 'E' + str(rowNum)
        if sheet[cell].value == None:
            #print("Empty cell: {}".format(cell))
            continue
        else:
            print()
            quant = 'G' + str(rowNum)
            cost = 'H' + str(rowNum)
            value = str(sheet[quant].value) + " ($" + str(sheet[cost].value) + ")"
            print("{}: {}".format(cell, sheet[cell].value))
            row2 += 1
            sheet2CellA = 'A' + str(row2)
            sheet2CellB = 'B' + str(row2)
              
            if sheet[cell].value.find(":") != -1:
                print("{}: {}".format(cell, sheet[cell].value[:sheet[cell].value.find(":")]))
                sheet2[sheet2CellA] = sheet[cell].value[:sheet[cell].value.find(":")]
                sheet2[sheet2CellB] = value
            else:
                print("{}: {}...{}".format(cell, sheet[cell].value[:30], value))
                sheet2[sheet2CellA] = sheet[cell].value[:30]
                sheet2[sheet2CellB] = value
    
    wb2.save('C:/Users/aj282/svhs.xlsx')

# Do not copy this formatting. RHS had significant formatting errors and is not replicable to other data sheets.
def getRhs():
    wb = openpyxl.load_workbook('C:/Users/aj282/Downloads/School budget proposals/School budget proposals/Ramapo Budget Principal 2020-2021.xlsx', data_only=True)

    sheet = wb['DO NOT MAKE ADDITIONAL SHEETS']

    #sheetsDict = {}

    rowNum = 1

    wb2 = openpyxl.Workbook()
    sheet2 = wb2.active
    sheet2.title = 'Aggregate'
    row2 = 1

    #Technology Hardware (Note: Other hardware/bad data to be filtered)
    for i in range(44,70):
        rowNum = i
        cell = 'B' + str(rowNum)
        if sheet[cell].value == None:
            #print("Empty cell: {}".format(cell))
            continue
        else:
            print()
            quant = 'H' + str(rowNum)
            cost = 'I' + str(rowNum)
            value = str(sheet[quant].value) + " ($" + str(sheet[cost].value) + ")"
            print("{}: {}".format(cell, sheet[cell].value))
            row2 += 1
            sheet2CellA = 'A' + str(row2)
            sheet2CellB = 'B' + str(row2)
              
            if sheet[cell].value.find(":") != -1:
                print("{}: {}".format(cell, sheet[cell].value[:sheet[cell].value.find(":")]))
                sheet2[sheet2CellA] = sheet[cell].value[:sheet[cell].value.find(":")]
                sheet2[sheet2CellB] = value
            else:
                print("{}: {}...{}".format(cell, sheet[cell].value[:30], value))
                sheet2[sheet2CellA] = sheet[cell].value[:30]
                sheet2[sheet2CellB] = value
            


    #Technology Software
    for i in range(72,86):
        print("\nBegin software\n")
        rowNum = i
        cell = 'F' + str(rowNum)
        if sheet[cell].value == None:
            #print("Empty cell: {}".format(cell))
            continue
        else:
            print()
            quant = 'H' + str(rowNum)
            cost = 'I' + str(rowNum)
            value = str(sheet[quant].value) + " ($" + str(sheet[cost].value) + ")"
            print("{}: {}".format(cell, sheet[cell].value))
            row2 += 1
            sheet2CellA = 'A' + str(row2)
            sheet2CellB = 'B' + str(row2)
              
            if sheet[cell].value.find(":") != -1:
                print("{}: {}".format(cell, sheet[cell].value[:sheet[cell].value.find(":")]))
                sheet2[sheet2CellA] = sheet[cell].value[:sheet[cell].value.find(":")]
                sheet2[sheet2CellB] = value
            else:
                print("{}: {}...{}".format(cell, sheet[cell].value[:30], value))
                sheet2[sheet2CellA] = sheet[cell].value[:30]
                sheet2[sheet2CellB] = value
    
    wb2.save('C:/Users/aj282/rhs.xlsx')


if __name__ == '__main__':
    #getKakiat()
    #getSvhs()
    getRhs()
        






