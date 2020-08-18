score = int(input("請輸入成績:"))
if score >= 0 and score <= 100:
    if score >=90:
        print("等級A")
    elif score >=80:
        print("等級B")
    elif score >=70:
        print("等級C")
    elif score >=60:
        print("等級D")
    else:
        print("等級E")
else:
        print("輸入錯誤")