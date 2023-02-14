# 상대경로가 파일 실행중 모호해지면서 파일을 찾지 못함
# 실행파일과 모듈로 구분하여 문제를 해결할 예정
# error:has no attribute 'CLSIDToClassMap' 발생시 appdata - local - temp 폴더에 있는 gen_py 폴더 삭제후 파이참 재시작

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