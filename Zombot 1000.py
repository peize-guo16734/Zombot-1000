print("Title of program: Zombot 1000")
print()
while True:
  description = input("How do you feel?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("Be positive, you can do it!")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Good job, keep it up!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("You might need a rest, you can continue with work later.")
      counter += 1

  if counter == 0:
    
      output = "ERROR 404 please try again."

  elif counter == 1:
    
      output = "Looks like you are feeling " + feelings_list[0] + ". Please "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
