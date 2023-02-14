import os
import win32com.client as win32
hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwp.Run("FileNew")
hwp.RegisterModule("FilePathCheckDLL", "SecurityModule")
hwp.Open(r"./상장샘플.hwp")

BASE_DIR = r"./첨부"
첨부파일리스트 = os.listdir(r"./첨부")

def 첨부삽입(path):
    hwp.HAction.GetDefault("InsertFile", hwp.HParameterSet.HInsertFile.HSet)
    hwp.HParameterSet.HInsertFile.filename = path
    hwp.HParameterSet.HInsertFile.KeepSection = 1
    hwp.HParameterSet.HInsertFile.KeepCharshape = 1
    hwp.HParameterSet.HInsertFile.KeepParashape = 1
    hwp.HParameterSet.HInsertFile.KeepStyle = 1
    hwp.HAction.Execute("InsertFile", hwp.HParameterSet.HInsertFile.HSet)
    return

hwp.MovePos(3)

for i in 첨부파일리스트:
    첨부삽입(os.path.join(BASE_DIR, i))
    hwp.MovePos(3)

hwp.Quit()