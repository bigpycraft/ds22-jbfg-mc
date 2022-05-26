def read_csv(filename):
    # 파일데이터 읽어오기
    fp = open(filename, "r", encoding = "utf-8")
    data = fp.read()
    fp.close()

    users = data.split(",") # 데이터를 구분하여 리스트로 담기
    return users
