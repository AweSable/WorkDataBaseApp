import os, re
def saveSubdir(directory, file):
	dir=directory
	myfile=file
	regWasteDoc=re.compile(' ВП[ ,_]|ПСИ| РЭ[ ,_]| ГЧ[ ,_]| Д\d\d?[ ,_]| РР\d\d?[ ,_]| ГЧ[ ,_]| ПМ[ ,_]|[П,п]огашенн?ые|[А,а]нн?лированн?ые|[З,з]амен[е,ё]нн?ые')
	regPartIndexVar1=re.compile('^ЦДЛР[ ,\.](\d\d\d\d\.\d\d\.\d\d\.\d\d\d*).+')
	regPartIndexVar2=re.compile('^(\d\d\d\d\.\d\d\.\d\d\.\d\d\d).+')
	regPartIndexVar3=re.compile('^(\d\d\d\d\-\d\d\.\d\d\.\d\d\.\d\d\d).+')
	MatchVar1=False
	MatchVar2=False
	MatchVar3=False
	for (thisDir, SubHere, filesHere) in os.walk(dir):
		for filename in filesHere:
			MatchWasteDoc=regWasteDoc.search(filename)
			MatchVar1=regPartIndexVar1.search(filename)
			MatchVar2=regPartIndexVar2.search(filename)
			MatchVar3=regPartIndexVar3.search(filename)
			Bol=MatchVar1 or MatchVar2 or MatchVar3
			if MatchWasteDoc==None and Bol:
				if regPartIndexVar1.search(filename):
					matchPartIndex=regPartIndexVar1.match(filename)
					sPartIndex=matchPartIndex.group(1)
				elif regPartIndexVar2.search(filename):
					matchPartIndex=regPartIndexVar2.match(filename)
					sPartIndex=matchPartIndex.group(1)
				elif regPartIndexVar3.search(filename):
					matchPartIndex=regPartIndexVar3.match(filename)
					sPartIndex=matchPartIndex.group(1)
				ref='@#'+os.path.join(thisDir, filename)+'#'
				record=ref+';'+filename[:-4]+';'+thisDir+';'+sPartIndex+'\n'
				myfile.write(record.encode())
			MatchVar1=False
			MatchVar2=False
			MatchVar3=False
	
drawingdirs = []
drawingdirs.insert(0,r'R:\Специальные документы\1402 Архив КД продукта')
drawingdirs.insert(1,r'R:\Специальные документы\1402 ТСМ Архив КД продукта')
drawingdirs.insert(2,r'R:\Специальные документы\1402 ТХМ Архив КД продукта')
drawingdirs.insert(3,r'R:\Специальные документы\1402 Проекты извещений')
#drawingdirs.insert(4,r'R:\Специальные документы\1402 Архив КД оснастки\ОСНАСТКА')
#drawingdirs.insert(5,r'R:\Специальные документы\1402 Архив КД оснастки\ОСНАСТКА_ДНПиПП\7800\7800-0084.00.00.000_Оснастка прокатная ВСО-3907')

myfile = open(r'D:\Резка\БД\references.txt', 'wb')
for	dir in drawingdirs:
	saveSubdir(dir, myfile)
myfile.close()

sketchesdir=r'R:\Специальные документы\1421 Карты эскизов к ТП заготовительного производства'
myfile = open(r'D:\Резка\БД\referencesSketches.txt', 'wb')
saveSubdir(sketchesdir, myfile)
myfile.close()