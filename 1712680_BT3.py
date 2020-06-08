#list end signature
lEndSign=['.',';','!','?']
#acronym file
norAcronym='normalAcronym.txt'
nameAcronym='nameAcronym.txt'
numAcronym='numberAcronym.txt'
otherAcronym='otherAcronym.txt'
listfileInput=[nameAcronym,numAcronym,otherAcronym]

#Return 'list' KQ vị trí rất cả các dấu hiệu kết thúc câu
def findEndSign(iText: str):
    lPositionEndSign=[]
    for i in range(0,len(iText)-1):
        if iText[i] in lEndSign and iText[i+1] == ' ':
            lPositionEndSign.append(i)
    return lPositionEndSign

#Return 'list' TỪ trước và sau dấu '.'
def getEndWord(iText: str, lEndSign: list):
    ListOfEndWord = []
    for i in lEndSign:
        position1 = iText[:i].rfind(' ') + 1
        position2 = iText[i+2:].find(' ') + i + 2
        #Xử lý trường hợp "### TP. HCM. ###"
        temp = iText[i+2:].find('.') + i + 2
        if temp < position2:
            position2 = temp
        ListOfEndWord.append(iText[position1:position2])
    # print(ListOfEndWord)
    return ListOfEndWord
        
def CheckAcronym(ListOfEndWord: list):
    lAcronym1=[]
    lAcronym2=[]
    Outlist=[]

    f = open(norAcronym, 'rt', encoding= 'utf-8')
    for i in f:
        i = i.replace('\n','')
        lAcronym1.append(i)
    f.close()
     
    for namefile in listfileInput:
        f = open(namefile, 'rt', encoding= 'utf-8')
        for i in f:
            i = i.replace('\n','')
            lAcronym2.append(i)
        f.close()

    for i in ListOfEndWord:
        flat = 0
        temp = i[:i.find(' ')]
        if temp in lAcronym1:
            Outlist.append(0)
            flat = 1
            continue
        for j in lAcronym2:
            if i in j:
                Outlist.append(0)
                flat = 1
                break 
        if flat == 0:
            Outlist.append(1)
    # print(Outlist)
    return Outlist

#Run here
#input text
iText = 'TS. Ng. V. A cùng ThS. B đã nghiên cứu thành công vacxin. TP. HCM phối hợp với Q. Tân Bình, Q. Tân Phú thực hiện thử nghiệm trên chuột.'
# iText = 'Nếu ai đó hỏi tôi, cuốn sách nào bạn muốn giới thiệu cho mọi người nhất, tôi sẽ không ngần ngại trả lời “Harry Potter”. Lần đầu tiên tôi biết đến tác phẩm này qua sự giới thiệu của bạn tôi. Đọc xong tập một tôi tự hỏi, không biết những tập sau tác giả viết gì mà đến bảy tập. Nhưng rồi tôi đã tìm được câu trả lời: tập sau hay hơn tập trước, càng về sau càng hay khi các bí mật dần dần được tiết lộ. Đó chính là sức hút độc đáo của tác phẩm.'

lPositionEndSign = findEndSign(iText)
lEndWord = getEndWord(iText,lPositionEndSign)
lIsRealEnd = CheckAcronym(lEndWord)
result = []
position = 0
for i in range(len(lPositionEndSign)):
    if lIsRealEnd[i]==1:
        result.append(iText[position:lPositionEndSign[i]+1])
        position = lPositionEndSign[i]+2
    else:
        continue
result.append(iText[position:])

#print result
for i in result:
    print(i)

