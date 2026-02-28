#글자 수 세기 프로그램, 공백 포함, 공백 미포함
while True:
  try:
    str=input("글자수를 세고자 하는 텍스트를 입력하세요 : ")

    len_all=len(str.strip())
    len_wo_space=len(str.strip().replace(" ",""))
  except:
    print("무언가 잘못 입력했으니 다시 해보세요")

  print(f"공백을 포함한 문자의 개수는 {len_all}개입니다.")
  print(f"공백을 포함하지 않은 문자의 개수는 {len_wo_space}개입니다.")