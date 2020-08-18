math_score = int(input("請輸入數學成績:"))
english_score = int(input("請輸入英文成績:"))
if math_score >= 0 and english_score >= 0 and math_score <= 100 and english_score <= 100:
    if math_score >= 90 and english_score >= 90:
        print("有獎品")
    elif math_score <= 60 and english_score <= 60:
        print("要處罰")
    elif math_score <= 60 or english_score <= 60:
        print("再加油")
else:
    print("輸入錯誤")